# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimaxapprox(RPackage):
	"""Implementation of Remez Algorithm for Polynomial and Rational
Function Approximation

	Implements the algorithm of Remez (1962) for polynomial minimax
    approximation and of Cody et al. (1968) <doi:10.1007/BF02162506> for
    rational minimax approximation.
	"""
	
	homepage = "https://github.com/aadler/MiniMaxApprox"
	cran = "minimaxApprox" 

	version("0.3.0", md5="6ce7cd3c0041dc1757dfbb98ad8bc5da")

