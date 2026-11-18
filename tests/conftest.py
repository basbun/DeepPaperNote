from __future__ import annotations

import os
import sys
from pathlib import Path


# Keep the developer's own DeepPaperNote settings out of the test run. The skill
# reads DEEPPAPERNOTE_* from the environment and, as a fallback, from ~/.zshenv
# and friends, and some modules resolve them at import time, so this must run
# before any test module is collected. A machine with
# DEEPPAPERNOTE_OUTPUT_LANGUAGE=en in ~/.zshenv failed 46 tests that assume the
# zh-CN default. Subprocess tests inherit this environment.
for _name in [n for n in os.environ if n.startswith("DEEPPAPERNOTE_")]:
    del os.environ[_name]
# The skill's own switch for the shell-file fallback. Tests of the fallback
# itself delete it with monkeypatch.
os.environ["DEEPPAPERNOTE_DISABLE_SHELL_CONFIG"] = "1"


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / "skills" / "deeppapernote" / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
# Repo root, appended (not first) so `scripts.generate_star_history` imports
# without shadowing the skill's own modules.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
