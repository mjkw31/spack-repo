# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBretigea(RPackage):
	"""Brain Cell Type Specific Gene Expression Analysis

	Analysis of relative cell type proportions in bulk gene expression data. Provides a well-validated set of brain cell type-specific marker genes derived from multiple types of experiments, as described in McKenzie (2018) <doi:10.1038/s41598-018-27293-5>. For brain tissue data sets, there are marker genes available for astrocytes, endothelial cells, microglia, neurons, oligodendrocytes, and oligodendrocyte precursor cells, derived from each of human, mice, and combination human/mouse data sets. However, if you have access to your own marker genes, the functions can be applied to bulk gene expression data from any tissue. Also implements multiple options for relative cell type proportion estimation using these marker genes, adapting and expanding on approaches from the 'CellCODE' R package described in Chikina (2015) <doi:10.1093/bioinformatics/btv015>. The number of cell type marker genes used in a given analysis can be increased or decreased based on your preferences and the data set. Finally, provides functions to use the estimates to adjust for variability in the relative proportion of cell types across samples prior to downstream analyses.
	"""
	
	cran = "BRETIGEA" 

	version("1.0.3", md5="adbcf39a21afbb0bddcdff7504ed8763")

	depends_on("r@3:", type=("build", "run"))
