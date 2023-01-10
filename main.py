import  metaData
import metaData.extractTitleAndSourceFromArabicDataset as ex
import  metaData.metaData as md
import metaData.keyWords as kw
import metaData.keyWordsUsingYake as kwy
# you should change all pathes to your pc path to avoid errors , you will find arabiya data set in this repo
filePath = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Politics\\#تركيا-تستهدف-داعش-والعمال-الكردستاني-براً-وجواً-.txt"
path = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test\\Politics"
filename = "#تركيا-تستهدف-داعش-والعمال-الكردستاني-براً-وجواً-.txt"
body = ex.extractTitleAndPublisher(filePath)
md.get_file_metadata(path, filename)
keywords = kw.get_keywordsFromText(body)
kw.print_results(keywords)
keywords = kwy.yakeKeyWords(body)
print(keywords)

