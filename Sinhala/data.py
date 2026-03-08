from datasets import Dataset
from datasets import load_dataset
from pandas import DataFrame as df 



class Data ():
    def sold():
        sold_train = Dataset.to_pandas(load_dataset('sinhala-nlp/SOLD', split='train'))
        sold_test = Dataset.to_pandas(load_dataset('sinhala-nlp/SOLD', split='test'))
        sold_test.to_csv('sold_test.csv', index=False)
        sold_train.to_csv('sold_train.csv', index=False)




    def SemiSOLD():

        semi_sold = Dataset.to_pandas(load_dataset('sinhala-nlp/SemiSOLD', split='train'))  
        semi_sold.to_csv('semi_sold.csv', index=False)