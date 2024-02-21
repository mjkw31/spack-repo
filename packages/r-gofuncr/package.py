# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofuncr(RPackage):
	"""Gene ontology enrichment using FUNC.

	GOfuncR performs a gene ontology enrichment analysis based on the
	ontology enrichment software FUNC. GO-annotations are obtained from
	OrganismDb or OrgDb packages ('Homo.sapiens' by default); the GO-graph
	is included in the package and updated regularly (27-Mar-2019). GOfuncR
	provides the standard candidate vs. background enrichment analysis using
	the hypergeometric test, as well as three additional tests: (i) the
	Wilcoxon rank-sum test that is used when genes are ranked, (ii) a
	binomial test that is used when genes are associated with two counts and
	(iii) a Chi-square or Fisher's exact test that is used in cases when
	genes are associated with four counts. To correct for multiple testing
	and interdependency of the tests, family-wise error rates are computed
	based on random permutations of the gene-associated variables. GOfuncR
	also provides tools for exploring the ontology graph and the
	annotations, and options to take gene-length or spatial clustering of
	genes into account. It is also possible to provide custom gene
	coordinates, annotations and ontologies."""

	bioc = "GOfuncR"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GOfuncR_1.22.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GOfuncR/GOfuncR_1.22.2.tar.gz"]

	version("1.22.2", md5="d1b00ef5711c3012a11f52cc7312d60b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-vioplot@0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mapplots@1.5:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.28.4:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
