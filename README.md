[![Generic badge](https://img.shields.io/badge/ENSAE-ML%20for%20NLP-blue.svg)](https://shields.io/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-red.svg)](#python) [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qrKfXM04D2GN3uQBcbMVCFrUkhhVlV3s?usp=sharing)

# Sequence generation model for replicating phraseological patterns from an homegenous political group

**The report linked to this repository is available [here](final_report.pdf)**

**The colab is available [here](https://colab.research.google.com/drive/1qrKfXM04D2GN3uQBcbMVCFrUkhhVlV3s?usp=sharing)**

## Overview
In this work, we attempted to create a sequence-generation model that aims to replicate phrase-ologic patterns from an homegenous
political group. Our main motivation is to investigate the ability of our model to simulate thematic discourse and subtle languages nuances that could pass as genuine. Thereby, our project is structured around the following question : is it possible to create bots that could actually perform *astroturfing* and interfere in the political/social debate with relatively modest data and modelling techniques ?


## Architecture

The architecture we used is a pre-trained GPT-2 model that we fine-tuned on 30k French tweets from pro-Zemmour people. We used a simple baseline model of 3 LSTM layers to compare the results. We also used qualitative (rating) and quantitative (BERTScore) metrics.

![Alt text](img/models.png?raw=true "Architecture models")


## Results

The GPT-2 model gave use astonishing results. Even though it is not that better than the baseline quantitatively, we clearly see a difference qualitatively. 
Here a some astonishing, or even frightening, generated sentences

* >L'islamisme est une secte qui veut détruire les
communautés chrétiennes.
* >La France doit se lever et se mobiliser contre
la folie meurtrière de donald trump
* >L'immigration est un danger et ça veut dire
que les français ont besoin de l'aide.
* >L'immigration est une des principales raisons
de l'échec de la france
* >L'islamisme se fonde sur la peur, le mépris et
le désarroi.
* >La liberté de religion ne doit être accordé en
aucune manière. vous n'avez aucun avenir.

A few more examples are available in the appendix of the report.


## Discussion

We were able to generate an interesting but rather
modest proportion of astonishingly accurate
tweets in terms of the replication of the political
discourse we targeted (see appendix). The GPT2
model ability to capture themes as well as syntax
and writing style opens the door for astroturfing
even with small resources and limited data.
A direct improvement path would consist in
scaling the complexity of the model and the size
of the dataset i.e bigger GPT2 model fine-tuned
on TBs of french data and millions of relevant
tweets. Having the ability to generate a significant
proportion of precisely replicated tweets will rise
serious ethical concerns as it directly opens the
door for mass manipulation on social media. This
work really allowed us to understand the power of
NLP tools and the sheer necessity to poise it with
responsibility and an increased consciousness
when we deal with online content.
