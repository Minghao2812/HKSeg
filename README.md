# HKSeg

It's a collaborative ongoing work.  
$\dag$ Mainly contributed by [Minghao](https://github.com/Minghao2812)  
$\ddag$ Mainly contributed by [Randy](https://github.com/randylinhustle)

## Dictionary

- dict_celebrity $\dag$
  - Hong Kong celebrity
- dict_institution $\dag$
- dict_location_hk $\dag$
  - Includes locations related to Hong Kong. They don't have to be in Hong Kong physically.
- dict_politics $\ddag$
- dict_covid19_vaccine $\dag$
- dict_covid19 $\dag$
- dict_general_en $\ddag$ $\dag$
- dict_general_zh $\ddag$ $\dag$

## Stopword

- ad_words $\dag$
  - Summaried keywords related to advertisement and promotional contents appears frequently in Hong Kong public media.
  - Keywords are in regular expression format.
- stopwords_canto $\ddag$ $\dag$
  - Stopwords in Cantonese.
- stopwords_en $\ddag$ $\dag$
  - Stopwords in English.
- stopwords_simple $\dag$
  - A simplified list of Cantonese stopwords. Numbers are included.

## jieba tools

- jieba_formatter.py $\dag$
  - A script made for solving a mistake when loading user-defined dictionary with jieba (jieba3k 0.35.1).
