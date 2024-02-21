# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfa(RPackage):
	"""Detrended Fluctuation Analysis

	Contains the Detrended Fluctuation Analysis (DFA), Detrended Cross-Correlation Analysis (DCCA), Detrended Cross-Correlation Coefficient (rhoDCCA), Delta Amplitude Detrended Cross-Correlation Coefficient (DeltarhoDCCA), log amplitude Detrended Fluctuation Analysis (DeltalogDFA), two DFA automatic methods for identification of crossover points and a Deltalog automatic method for identification of reference channels.
	"""
	
	cran = "DFA" 

	version("0.9.0", md5="ff7d791379b70da06bb3215b2ebfd89d")

	depends_on("r@2.10:", type=("build", "run"))
