# Lint as: python3
# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Util classes and functions."""

from __future__ import absolute_import
from __future__ import division
# from __future__ import google_type_annotations
from __future__ import print_function

# pylint: disable=g-direct-tensorflow-import
from tensorflow.python.training.tracking import tracking


class VolatileTrackable(tracking.AutoTrackable):
  """A util class to keep Trackables that might change instances."""

  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)

  def reassign_trackable(self, **kwargs):
    for k, v in kwargs.items():
      delattr(self, k)  # untrack this object
      setattr(self, k, v)  # track the new object
