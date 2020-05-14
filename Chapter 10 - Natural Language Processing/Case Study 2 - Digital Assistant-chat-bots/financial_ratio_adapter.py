
import spacy
import random
from itertools import product

from spacy.util import minibatch, compounding
from chatterbot.logic import LogicAdapter

#Step 3: Data Preparation
#We want our chatbot to be able to distinguish between subtle 
#inquires. For example – One might want to ask about the company 
#Apple Inc by simply referring to it as Apple. In either case, 
#we want to map it to a ticker, AAPL in this case. Constructing 
#commonly used phrases in order to refer to firms can be built by 
#using a dictionary such as
companies = {
    'AAPL':  ['Apple', 'Apple Inc'],
    'BAC': ['BAML', 'BofA', 'Bank of America'],
    'C': ['Citi', 'Citibank'],
    'DAL': ['Delta', 'Delta Airlines']
}

ratios = {
    'return-on-equity-ttm': ['ROE', 'Return on Equity'],
    'cash-from-operations-quarterly': ['CFO', 'Cash Flow from Operations'],
    'pe-ratio-ttm': ['PE', 'Price to equity', 'pe ratio'],
    'revenue-ttm': ['Sales', 'Revenue'],
}

string_templates = ['Get me the {ratio} for {company}',
                   'What is the {ratio} for {company}?',
                   'Tell me the {ratio} for {company}',
                  ] 
#Step 4: Model construction and training
#Step 4.1 Model construction 
companies_rev = {}
for k, v in companies.items():
    for ve in v:
        companies_rev[ve] = k
        
ratios_rev = {}
for k, v in ratios.items():
    for ve in v:
        ratios_rev[ve] = k

companies_list = list(companies_rev.keys())
ratios_list = list(ratios_rev.keys())

#Next, we to create sample statements for our model. 
#We contract a function in order to give us a random sentence structure, 
#inquiring about a random financial ratio for a random company We will be 
#creating a custom Named Entity Recognition model in the spacy framework. 
N_training_samples = 100

def get_training_sample(string_templates, ratios_list, companies_list):
    string_template=string_templates[random.randint(0, len(string_templates)-1)]
    ratio = ratios_list[random.randint(0, len(ratios_list)-1)]
    company = companies_list[random.randint(0, len(companies_list)-1)]
    sent = string_template.format(ratio=ratio,company=company)
    ents = {"entities": [(sent.index(ratio), sent.index(ratio)+len(ratio), 'RATIO'),
                         (sent.index(company), sent.index(company)+len(company), 'COMPANY')
                        ]}
    return (sent, ents)

#Defining the training data.
TRAIN_DATA = [
    get_training_sample(string_templates, ratios_list, companies_list) for i in range(N_training_samples)
]
#4.2. Setting the optimizer and Logical Adapter 
#First, we construct a blank model in spacy spaCy’s models are statistical 
#and every “decision” they make. Training the NER model is akin to updating 
#the weights for each token. The most important step is to use a good optimizer. 
nlp = spacy.blank("en")

ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

ner.add_label('RATIO')
ner.add_label('COMPANY')

optimizer = nlp.begin_training()

move_names = list(ner.move_names)
# get names of other pipes to disable them during training
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
with nlp.disable_pipes(*other_pipes):  # only train NER
    sizes = compounding(1.0, 4.0, 1.001)
    # batch up the examples using spaCy's minibatch
    for itn in range(30):
        random.shuffle(TRAIN_DATA)
        batches = minibatch(TRAIN_DATA, size=sizes)
        losses = {}
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
        print("Losses", losses)


#Setting the Logic Adapter
class FinancialRatioAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super(FinancialRatioAdapter, self).__init__(chatbot, **kwargs)

    def process(self, statement, additional_response_selection_parameters):
        """
        Returns the value.
        """
        from chatterbot.conversation import Statement

        user_input = statement.text

        doc = nlp(user_input)
        company = None
        ratio = None
        confidence = 0

        # We need exactly 1 company and one ratio
        if len(doc.ents) == 2:
            for ent in doc.ents:
                if ent.label_ == "RATIO":
                    ratio = ent.text
                    if ratio in ratios_rev:
                        confidence += 0.5
                if ent.label_ == "COMPANY":
                    company = ent.text
                    if company in companies_rev:
                        confidence += 0.5

        if confidence > 0.99:
            outtext = '''https://www.zacks.com/stock/chart/{company}/fundamental/{ratio}
					  '''.format(ratio=ratios_rev[ratio], company=companies_rev[company])
            confidence = 1
        else:
            outtext = 'Sorry! Could not figure out what the user wants'
            confidence = 0

        output_statement = Statement(text=outtext)
        output_statement.confidence = confidence

        return output_statement