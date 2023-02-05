structName = 123
structattr = 456

headText = f"pybind11::class_<{structName}>(m, \"{structName}\")"
midText1 = "    .def(pybind11::init())"
midText2 = f"    .def_readwrite(\"{structattr}\", &{structName}::{structattr})"
