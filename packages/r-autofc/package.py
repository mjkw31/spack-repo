# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutofc(RPackage):
	"""Automatic Construction of Forced-Choice Tests

	Forced-choice (FC) response has gained increasing popularity and interest for its resistance to faking when well-designed (Cao & Drasgow, 2019 <doi:10.1037/apl0000414>). To established well-designed FC scales, typically each item within a block should measure different trait and have similar level of social desirability (Zhang et al., 2020 <doi:10.1177/1094428119836486>). Recent study also suggests the importance of high inter-item agreement of social desirability between items within a block (Pavlov et al., 2021 <doi:10.31234/osf.io/hmnrc>). In addition to this, FC developers may also need to maximize factor loading differences (Brown & Maydeu-Olivares, 2011 <doi:10.1177/0013164410375112>) or minimize item location differences (Cao & Drasgow, 2019 <doi:10.1037/apl0000414>) depending on scoring models. Decision of which items should be assigned to the same block, termed item pairing, is thus critical to the quality of an FC test. This pairing process is essentially an optimization process which is currently carried out manually. However, given that we often need to simultaneously meet multiple objectives, manual pairing becomes impractical or even not feasible once the number of latent traits and/or number of items per trait are relatively large. To address these problems, autoFC is developed as a practical tool for facilitating the automatic construction of FC tests, essentially exempting users from the burden of manual item pairing and reducing the computational costs and biases induced by simple ranking methods. Given characteristics of each item (and item responses), FC tests can be automatically constructed based on user-defined pairing criteria and weights as well as customized optimization behavior. Users can also construct parallel forms of the same test following the same pairing rules.
	"""
	
	homepage = "https://github.com/tspsyched/autoFC"
	cran = "autoFC" 

	version("0.1.2", md5="5f91b95f5561493d77e7429cc5db52cd")

	depends_on("r-irrcac", type=("build", "run"))
