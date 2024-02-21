# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgstat(RPackage):
	"""Amos Tanay's Group High Performance Statistical Utilities

	A collection of high performance utilities to compute
    distance, correlation, auto correlation, clustering and other tasks.
    Contains graph clustering algorithm described in "MetaCell: analysis
    of single-cell RNA-seq data using K-nn graph partitions" (Yael Baran,
    Akhiad Bercovich, Arnau Sebe-Pedros, Yaniv Lubling, Amir Giladi, Elad
    Chomsky, Zohar Meir, Michael Hoichman, Aviezer Lifshitz & Amos Tanay,
    2019 <doi:10.1186/s13059-019-1812-2>).
	"""
	
	cran = "tgstat" 

	version("2.3.25", md5="d68ac0356a3704f93f11f3cc9c34f14d")

	depends_on("r@3.5:", type=("build", "run"))
