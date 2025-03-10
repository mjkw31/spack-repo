# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyMochi(PythonPackage):
    """MoCHI: Neural networks to quantify energies, energetic couplings, epistasis and allostery from deep mutational scanning data."""

    homepage = "https://github.com/lehner-lab/MoCHI"
    git = "https://github.com/lehner-lab/MoCHI"

    version("0.9", tag="v0.9")

    depends_on("python@3.9.9", type=("build", "run"))

    #depends_on("py-jupyter-client", type=("build", "run"))
    #depends_on("py-jupyter-core", type=("build", "run"))
    #depends_on("py-jupyter-server", type=("build", "run"))
    #depends_on("py-jupyterlab", type=("build", "run"))
    depends_on("py-pandas@1.4.2", type=("build", "run"))
    depends_on("py-matplotlib@3.5.1", type=("build", "run"))
    depends_on("py-numpy@1.21.2", type=("build", "run"))
    depends_on("py-pyreadr@0.4.4", type=("build", "run"))
    depends_on("py-torch@1.10.1", type=("build", "run"))
    depends_on("py-scikit-learn@1.0.2", type=("build", "run"))
    depends_on("py-scipy@1.8.0", type=("build", "run"))
    depends_on("py-seaborn@0.11.2", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    #variant("cxxstd", default=False, values=("14"), description="Use the specified C++ standard when building.")
    #depends_on("protobuf@3.20.3", type=("build", "run"))

    depends_on("gcc")
    depends_on("freetype")

    @run_after("install")
    def bin_install(self):
        #mkdir(self.prefix.bin)
        with open(self.prefix.bin + "/run_mochi.py", "w") as f:
            f.write("#!/bin/bash\necho -e \"from pymochi import main\\nimport sys\\nsys.exit(main.main())\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + "\" python3.9 - \"$@\"")

        with open(self.prefix.bin + "/demo_mochi.py", "w") as f:
            f.write("#!/bin/bash\necho -e \"from pymochi import main\\nimport sys\\nsys.exit(main.main(demo_mode = True))\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + "\" python3.9 - \"$@\"")

        os.chmod(self.prefix.bin + "/run_mochi.py", 0o755)
        os.chmod(self.prefix.bin + "/demo_mochi.py", 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)


