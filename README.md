# Benchmark data sets for Knowledge Graph-based Similarity

We  present  a  collection  of  21  benchmark  data  sets  that  aim  at  circumventing the difficulties in building benchmarks for large biomedical knowledge graphs by exploiting proxies for biomedical entity similarity. An overview is shown below.

| Species         | Proteins | Pairs | Proteins | Pairs |
|-----------------|----------|-------|----------|-------|
| D. melanogaster | 481      | 397   | 335      | 270   |
| E. coli         | 371      | 738   | 264      | 428   |
| H. sapiens      | 7644     | 44677 | 7149     | 42204 |
| S. cerevisae    | 3874     | 34772 | 2959     | 21577 |
| All             | 12370    | 80584 | 10707    | 64479 |

## Prerequisites

To allow a direct comparison with the pre-computed semantic similarity measures, as well as facilitate the direct comparison between different works without needing to implement and/or compute the results, the KG data below should be downloaded and used.

* [Gene Ontology](https://github.com/liseda-lab/kgsim-benchmark/blob/master/GO/go-basic.zip)
* [Gene Ontology Annotations](https://github.com/liseda-lab/kgsim-benchmark/tree/master/GO) 
* [Human Phenotype Ontology](https://github.com/liseda-lab/kgsim-benchmark/blob/master/HPO/hp.obo) 
* [Human Phenotype Ontology Annotations](https://github.com/liseda-lab/kgsim-benchmark/blob/master/HPO/ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt) 


### Using the benchmark data sets for the evaluation of a novel semantic similarity measure

The steps to perform the benchmark evaluation for a new KG-based semantic similarity measures are as follows:

* Select the benchmark [data sets](https://github.com/liseda-lab/kgsim-benchmark/tree/master/Data%20Sets) that will be used;

* Using your novel measure, calculate the similarity for all entity pairs in the benchmark data sets using the benchmark KG;

* Compute evaluation metrics against proxy similarity values and representative semantic similarity scores;

* Upload the novel semantic similarity results to a data sharing platform, to support future direct comparisons.


## Authors

* **Carlota Cardoso** 
* **Rita Sousa**
* **Cátia Pesquita** 


## License
See the [LICENSE.md](https://github.com/liseda-lab/kgsim-benchmark/blob/master/LICENSE.md/LICENSE.md) file for details.


## Acknowledgments

This project was funded by the Portuguese FCT through the LASIGE Research Unit (UID/CEC/00408/2019), and also by the SMILAX project (PTDC/EEI-ESS/4633/2014).
