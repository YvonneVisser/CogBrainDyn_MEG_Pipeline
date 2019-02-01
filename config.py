"""
===========
Config file
===========

Configuration parameters for the study. This should be in a folder called
``library/`` inside the ``processing/`` directory.
"""

import os
import numpy as np


###############################################################################
# DIRECTORIES
# -----------
# Let's set the `study path`` where the data is stored on your system
study_path = 'E:/Neurospin/TimeLimit/Data'


# The ``subjects_dir`` and ``meg_dir`` for reading anatomical and MEG files.
# timelimit edit: only meg data in study folder, no need to differentiate

#subjects_dir = os.path.join(study_path, 'subjects')
#meg_dir = os.path.join(study_path, 'MEG')

###############################################################################
# DEFINE SUBJECTS
# ---------------
#
# A list of ``subject names``
# These are the ``nips`` in neurospin lingo

# XXX how to write this if we want to process only one subject?
# subjects = 'sample'

subjects = ('subj01', 'subj02', 'subj03')
'''
# 'subj05', 'subj06',
            'subj07', 'subj08', 'subj09', 'subj10', 'subj11',
             'subj12', 'subj13', 'subj14', 'subj15', 'subj16',
             'subj17', 'subj18', 'subj19', 'subj20', 'subj21', 
             'subj22')
'''

# ``bad subjects``  that should not be included in the analysis
exclude_subjects = {'subj01_noHPI'}

# # ``bad subjects``  that should not be included in the analysis
# exclude_subjects = {'subject_01', 'subject_09', 'subject_24'}

###############################################################################
# BAD CHANNELS
# ------------
#
# ``bad channels``, to be removed before maxfilter is applied
# you either get them from your recording notes, or from visualizing the data

bads = dict(subj01_noHPI=['MEG0213', 'MEG0731', 'MEG2217'],
            subj02=['MEG0213', 'MEG1422', 'MEG2141'],
            subj03=['MEG0213', 'MEG1932', 'MEG1923', 'MEG1442'])
'''
            subj04=[],
            subj05=[],
            subj06=[],
            subj07=[],
            subj08=[],
            subj09=[],
            subj10=[],
            subj11=[],
            subj12=[],
            subj13=[],
            subj14=[],
            subj15=[],
            subj16=[],
            subj17=[],
            subj18=[],
            subj19=[],
            subj20=[],
            subj21=[],
            subj22=[])
'''

###############################################################################
# DEFINE ADDITIONAL CHANNELS
# ------------
#
# Here you name/ replace  extra channels that were recorded, for instance EOG, ECG
# ``set_channel_types`` defines types of channels
# example : set_channel_types = {'EEG061': 'eog', 'EEG062': 'eog', 'EEG063': 'ecg', 'EEG064': 'misc'}
set_channel_types = None #{'EEG061': 'eog', 'EEG062': 'eog', 'EEG063': 'ecg', 'EEG064': 'emg'}

# ``rename_channels`` rename channels
# example : rename_channels = {'EEG061': 'EOG061', 'EEG062': 'EOG062', 'EEG063': 'ECG063'}
rename_channels = None #{'EEG061': 'EOG061', 'EEG062': 'EOG062', 'EEG063': 'ECG063', 'EEG064': 'EMG064'}


###############################################################################
# FREQUENCY FILTERING
# -------------------
#
# ``h_freq``  : the high-frequency cut-off in the lowpass filtering step.
# Keep it None if no lowpass filtering should be applied.
h_freq = None

# ``l_freq``  : the low-frequency cut-off in the highpass filtering step.
# Keep it None if no highpass filtering should be applied.
l_freq = 40.


###############################################################################
# MAXFILTER PARAMETERS
# -------------------
#
# Download the ``cross talk file`` and ``calibration file`` (these are machine specific)
# path:
# and place them in the study folder
ctc = os.path.join(os.path.dirname(__file__), 'ct_sparse.fif')
cal = os.path.join(os.path.dirname(__file__), 'sss_cal.dat')

# ``ref_run `` : defines the reference run used to adjust the head position for
# all other runs
mf_reference_run = 1

# ``st_duration `` : if None, no temporal-spatial filtering is applied during MaxFilter,
# otherwise, put a float that speficifies the buffer duration in seconds,
# Elekta default = 10s, meaning it acts like a 0.1 Hz highpass filter
st_duration = 30.



###############################################################################
# RESAMPLING
# ----------
#
# ``resample_sfreq``  : a float that specifies at which sampling frequency
# the data should be resampled. If None then no resampling will be done.
resample_sfreq = 256.


# ``decim`` : integer that says how much to decimate data at the epochs level.
# It is typically an alternative to the `resample_sfreq` parameter that
# can be used for resampling raw data.
decim = None


###############################################################################
# AUTOMATIC REJECTION OF ARTIFACTS
# --------------------------------
#
#  ``reject`` : the default rejection limits to make some epochs as bads.
# This allows to remove strong transient artifacts.
# **Note**: these numbers tend to vary between subjects.
reject = dict(meg=dict(mag=10e-12, grad=500e-12),
              eeg=dict(eeg=3000e-6))


###############################################################################
# EPOCHING
# --------
#
# ``tmin``: float that gives the start time before event of an epoch.
tmin = -1.

#  ``tmax`` : float that gives the end time after event of an epochs.
tmax = 2.

# ``baseline`` : tuple that specifies how to baseline the epochs; if None,
# no baseline is applied

baseline = (None, 0.)

#  `event_id`` : python dictionary that maps events (trigger/marker values)
# to conditions. E.g. `event_id = {'Auditory/Left': 1, 'Auditory/Right': 2}`

event_id = {'2s': 2, '4s': 3, '8s': 4, '16s': 5, 'Inf': 6, 'ClocksAppears': 7}
conditions = ['2s', '4s', '8s', '16s', 'Inf', 'ClockAppears']

###############################################################################
# ICA parameters
# --------------
# ``runica`` : boolean that says if ICA should be used or not.
runica = True

###############################################################################
# SOURCE SPACE PARAMETERS
# -----------------------
#

spacing = 'oct6'
mindist = 5
smooth = 10

fsaverage_vertices = [np.arange(10242), np.arange(10242)]

if not os.path.isdir(study_path):
    os.mkdir(study_path)

'''
if not os.path.isdir(subjects_dir):
    os.mkdir(subjects_dir)
'''

###############################################################################
# ADVANCED
# --------
#
# ``l_trans_bandwidth`` : float that specifies the transition bandwidth of the
# highpass filter. By default it's `'auto'` and uses default mne parameters.
l_trans_bandwidth = 'auto'

#  ``h_trans_bandwidth`` : float that specifies the transition bandwidth of the
# lowpass filter. By default it's `'auto'` and uses default mne parameters.
h_trans_bandwidth = 'auto'

#  ``N_JOBS`` : an integer that specifies how many subjects you want to run in parallel.
N_JOBS = 1
