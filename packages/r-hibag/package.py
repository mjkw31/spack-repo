# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHibag(RPackage):
	"""HLA Genotype Imputation with Attribute Bagging

	Imputes HLA classical alleles using GWAS SNP data, and it relies on a training set of HLA and SNP genotypes. HIBAG can be used by researchers with published parameter estimates instead of requiring access to large training sample datasets. It combines the concepts of attribute bagging, an ensemble classifier method, with haplotype inference for SNPs and HLA types. Attribute bagging is a technique which improves the accuracy and stability of classifier ensembles using bootstrap aggregating and random variable selection.
	"""
	
	homepage = "https://github.com/zhengxwen/HIBAG"
	bioc = "HIBAG"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HIBAG_1.38.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HIBAG/HIBAG_1.38.2.tar.gz"]

	version("1.38.2", md5="a45e528fc76fb752e54021bb438ff3fd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcppparallel@5:", type=("build", "run"))
