# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNrahdltp(RPackage):
	"""Location Tests for High-Dimensional Problems Including
Normal-Reference Approach

	We provide a collection of various classical tests and latest normal-reference approach tests for comparing high-dimensional mean vectors including two-sample and general linear hypothesis testing (GLHT) problem. The others’ tests for two-sample problem [see Bai, Zhidong, and Hewa Saranadasa.(1996) <https://www.jstor.org/stable/24306018>; Chen, Song Xi, and Ying-Li Qin.(2010) <doi:10.1214/09-aos716>; Srivastava, Muni S., and Meng Du.(2008) <doi:10.1016/j.jmva.2006.11.002>; Srivastava, Muni S., Shota Katayama, and Yutaka Kano.(2013)<doi:10.1016/j.jmva.2012.08.014>]. Normal-reference approach based tests for two-sample problem [see Zhang, Jin-Ting, Jia Guo, Bu Zhou, and Ming-Yen Cheng.(2020) <doi:10.1080/01621459.2019.1604366>; Zhang, Jin-Ting, Bu Zhou, Jia Guo, and Tianming Zhu.(2021) <doi:10.1016/j.jspi.2020.11.008>; Zhang, Liang, Tianming Zhu, and Jin-Ting Zhang.(2020) <doi:10.1016/j.ecosta.2019.12.002>; Zhang, Liang, Tianming Zhu, and Jin-Ting Zhang.(2023) <doi:10.1080/02664763.2020.1834516>; Zhang, Jin-Ting, and Tianming Zhu.(2022) <doi:10.1080/10485252.2021.2015768>; Zhang, Jin-Ting, and Tianming Zhu.(2022) <doi:10.1007/s42519-021-00232-w>; Zhu, Tianming, Pengfei Wang, and Jin-Ting Zhang.(2023) <doi:10.1007/s00180-023-01433-6>]. The others’ tests for GLHT problem [see Fujikoshi, Yasunori, Tetsuto Himeno, and Hirofumi Wakaki.(2004) <doi:10.14490/jjss.34.19>; Srivastava, Muni S., and Yasunori Fujikoshi.(2006) <doi:10.1016/j.jmva.2005.08.010>; Yamada, Takayuki, and Muni S. Srivastava.(2012) <doi:10.1080/03610926.2011.581786>; Schott, James R.(2007) <doi:10.1016/j.jmva.2006.11.007>; Zhou, Bu, Jia Guo, and Jin-Ting Zhang.(2017) <doi:10.1016/j.jspi.2017.03.005>]. Normal-reference approach based tests for GLHT problem [see Zhang, Jin-Ting, Jia Guo, and Bu Zhou.(2017) <doi:10.1016/j.jmva.2017.01.002>; Zhang, Jin-Ting, Bu Zhou, and Jia Guo.(2022) <doi:10.1016/j.jmva.2021.104816>; Zhu, Tianming, Liang Zhang, and Jin-Ting Zhang.(2022) <doi:10.5705/ss.202020.0362>; Zhu, Tianming, and Jin-Ting Zhang.(2022) <doi:10.1007/s00180-021-01110-6>; Zhang, Jin-Ting, and Tianming Zhu.(2022) <doi:10.1016/j.csda.2021.107385>].
	"""
	
	cran = "NRAHDLTP" 

	version("0.1.2", md5="d19a6344e71befb7a5ca0f63b148a5dc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
