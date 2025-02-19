from __future__ import annotations
import pathlib

CF_TYPY_MODE = "TYPY_MODE"
CF_TYPY_PY_APIPTR = "TYPY_PY_APIPTR"
CF_TYPY_PY_DLL = "TYPY_PY_DLL"
CF_TYPY_MODE_PYTHON = "PYTHON-BASED"
CF_TYPY_MODE_JULIA = "JULIA-BASED"
CF_TYPY_JL_EXE = "TYPY_JL_EXE"
CF_TYPY_JL_OPTS = "TYPY_JL_OPTS"
CF_JNUMPY_HOME = "JNUMPY_HOME"

TyPython_directory = (
    pathlib.Path(__file__).parent.absolute().joinpath("TyPython").as_posix()
)


InitTools_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("InitTools.jl").as_posix()
)


class SessionCtx:
    JULIA_EXE: str
    DEFAULT_PROJECT_DIR: str
    JULIA_START_OPTIONS: list[str]
