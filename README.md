# Benchmark data sets for Knowledge Graph-based Similarity

We  present  a  collection  of  21  benchmark  data  sets for evaluating semantic similarity measures for large biomedical knowledge graphs and ontologies. These datasets aim  at  circumventing the difficulties in building benchmarks for large biomedical knowledge graphs by exploiting proxies for biomedical entity similarity. An overview is shown below.

### Protein data sets
We created two different types of data sets according to the following criteria:
- _One aspect_: The proteins must have at least one annotation in one GO aspect.
- _All aspects_: The proteins must have at least one annotation in each GO aspect.

**Protein-protein interactions data sets**

_One aspect_

| Species         | Proteins | Pairs |
|:---------------:|:--------:|:-----:|
| D. melanogaster | 455      | 364   |
| E. coli         | 371      | 734   |
| H. sapiens      | 7093     | 30826 |
| S. cerevisae    | 3776     | 27898 |
| All             | 11695    | 59822 |

_All aspects_

| Species         | Proteins | Pairs |
|:---------------:|:--------:|:-----:|
| D. melanogaster | 287      | 200   |
| E. coli         | 263      | 420   |
| H. sapiens      | 6718     | 29672 |
| S. cerevisae    | 2888     | 16904 |
| All             | 10156    | 47196 |

**Molecular function data sets**

_One aspect_

| Species         | Proteins | Pairs  |
|:---------------:|:--------:|:------:|
| D. melanogaster | 7470     | 31350  |
| E. coli         | 1231     | 3363   | 
| H. sapiens      | 13246    | 31350  |
| S. cerevisae    | 4782     | 38166  |
| All             | 26729    | 104229 |

_All aspects_

| Species         | Proteins | Pairs  |
|:---------------:|:--------:|:------:|
| D. melanogaster | 5300     | 17682  |
| E. coli         | 724      | 1332   |
| H. sapiens      | 11666    | 25527  |
| S. cerevisae    | 3660     | 29265  |
| All             | 21350    | 73806  |

#### Protein data sets nomenclature

Data sets file names follow this structure **TYPE_SPECIESN.csv**
where:
* **TYPE**: Type of data set- MF for Molecular Function data sets and PPI for Protein-Protein Interaction data sets;
* **SPECIES**: Protein species in the data set- DM (_D. melanogaster_), EC (_E. Coli_), HS (_H. sapiens_), SC (_S. cerevisae_) and ALL (combining all four species); 
* **N**: annotation completness of the proteins in the data set-  1 for _One aspect_ proteins and 3 for _All aspects_ proteins.

### Genes-phenotypes data set

| Genes | Pairs |
|:-----:|:-----:|
| 2026  | 1200  |

## Prerequisites

To allow a direct comparison with the pre-computed semantic similarity measures, as well as facilitate the direct comparison between different works without needing to implement and/or compute the results, the KG data below should be downloaded and used.

* [Gene Ontology](https://github.com/liseda-lab/kgsim-benchmark/blob/master/GO) (available in OBO and OWL format)
* [Gene Ontology Annotations](https://github.com/liseda-lab/kgsim-benchmark/tree/master/GO) 
* [Human Phenotype Ontology](https://github.com/liseda-lab/kgsim-benchmark/blob/master/HPO) (available in OBO and OWL format)
* [Human Phenotype Ontology Annotations](https://github.com/liseda-lab/kgsim-benchmark/blob/master/HPO/ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt) 


### Using the benchmark data sets for the evaluation of a novel semantic similarity measure

The steps to perform the benchmark evaluation for a new KG-based semantic similarity measures are as follows:

* Select the benchmark [data sets](https://github.com/liseda-lab/kgsim-benchmark/tree/master/Data%20Sets) that will be used;

* Using your novel measure, calculate the similarity for all entity pairs in the benchmark data sets using the benchmark KG;

* Compute evaluation metrics against proxy similarity values and representative semantic similarity scores;

  These data sets support evaluation through simple correlation calculation between the novel measures and representative semantic similarity scores and proxy similarity values.  
  Additionally, the protein-protein interactions data sets can be used to evaluate the power of semantic similarity scores in predicting protein-protein interactions.
  Both evaluation techniques are supportedd by the [Jupyter Notebook](https://github.com/liseda-lab/kgsim-benchmark/tree/master/Jupyter%20Notebook) available in this repository.

* Upload the novel semantic similarity results to a data sharing platform, to support future direct comparisons, by forking this repository.

  The tables below provide an example of how to publish the results after using a protein-protein interaction data set to evaluate a novel semantic similarity measure.  

_Table 1_: Pearson Correlation coefficient between similarity proxies and semantic similarity measures.
  
| Similarity proxy          | BMA Resnik      |BMA Seco|GIC Resnik|GIC Seco   |New SSM  |
|:-------------------------:|:---------------:|:------:|:--------:|:---------:|:-------:|
|Sequence                   |0.215935         |0.199146|0.239537  |0.218870   | 0.11128 |
|Protein-protein interaction|0.625845	        |0.912552|0.915274  |0.996805	| 0.58274 |

Note that Pearson Correlation Coefficient scores have already been calculated for each data set's representative semantic similarity scores and similarity proxies. Find them [here](https://github.com/liseda-lab/kgsim-benchmark). 

_Table 2_: Predictive scores of the novel semantic similarity regarding protein-protein interaction. Threshold: minimum similarity for 2 proteins to be considered similar and to interact. Precision, Recall and F1 score: Performance evaluation metrics of the prediction.

| Threshold| Precision| Recall |F1 score|
|:--------:|:--------:|:------:|:------:|
| 0.5      | 0.6      | 0.45   | 0.514  |
| 0.6      |0.7       |0.58    |0.634   |
| 0.7      |0.7       |0.5     |0.59    | 
  

## Authors

* **Carlota Cardoso** 
* **Rita Sousa**
* **Cátia Pesquita** 


## License
See the [LICENSE.md](https://github.com/liseda-lab/kgsim-benchmark/blob/master/LICENSE.md/LICENSE.md) file for details.


## Acknowledgments

This project was funded by the Portuguese FCT through the LASIGE Research Unit (UID/CEC/00408/2019), and also by the SMILAX project (PTDC/EEI-ESS/4633/2014).
