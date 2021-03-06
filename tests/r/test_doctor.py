from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.doctor import doctor


def test_doctor():
  """Test module doctor.py by downloading
   doctor.csv and testing shape of
   extracted data has 485 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = doctor(test_path)
  try:
    assert x_train.shape == (485, 4)
  except:
    shutil.rmtree(test_path)
    raise()
