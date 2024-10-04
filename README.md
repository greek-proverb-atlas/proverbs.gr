# Towards a Greek Proverb Atlas: Computational Spatial Exploration and Attribution of Greek Proverbs

## Greek Proverb Exploration and Attribution
* Proverbs collected from the Hellenic Folklore Research Centre (http://www.kentrolaografias.gr). 
* The data are under a CC BY-NC-ND 4.0 licence (https://creativecommons.org/licenses/by-nc-nd/4.0/deed.el). 
* Only the text, the collector, and the place the proverb was collected from are used.
* We share [here](https://ipavlopoulos.github.io/paremia/data/) a subset of 11,500 proverbs, balanced across locations, used in our experiments.
* A preprint can be found in: https://www.researchsquare.com/article/rs-3360387/
* English translations of the balanced subset, using Llama-3.1-8B-Instruct, are included in the repository.

## The findings
* We show how proverbs are shared not only temporally, from generation to generation, but also spatially, from location to location.
* We share [a map of duplicates](https://nbviewer.org/github/ipavlopoulos/paremia/blob/main/misc/duplicates.html) we compiled. 
* We show [the spatial distribution](https://nbviewer.org/github/ipavlopoulos/paremia/blob/main/misc/frequent_places.html) of proverbs.
* We publish [a map with clickable pins](https://nbviewer.org/github/ipavlopoulos/paremia/blob/main/misc/frequent_ngrams.html), showing terms frequent in one location but not in the rest.
* We provide a benchmark in attribution.
* We use conformal prediction to attribute the possible locations of proverbs whose location was unregistered today.

---

Please cite us as: 
```
@inproceedings{pavlopoulos2024proverbs,
  title={Towards a Greek Proverb Atlas: A Computational Spatial Exploration and Attribution of Greek Proverbs},
  author={Pavlopoulos, John and Louridas, Panos and Filos, Panagiotis},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}
  year={2024}
}
```
