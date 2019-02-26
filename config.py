"""
===========
Config file
===========

Configuration parameters for the study. This should be in a folder called
``library/`` inside the ``processing/`` directory.
"""

import os
import numpy as np


# let the scripts generate plots or not
# execute %matplotlib qt in your command line once to show the figures in
# separate windows

plot = False

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
# SUBJECTS / RUNS
# ---------------
#
# The MEG-data need to be stored in a folder
# named my_study_path/MEG/my_subject/

# This is the name of your experimnet
study_name = 'timelimit'

# To define the subjects, we use a list with all the subject names. Even if its
# a single subject, it needs to be set up as a list with a single element,
# as in the example

subjects_list = ['s03']
'''
# 's01, s02'
# 's04, s05', 's06',
            's07', 's08', 's09', 's10', 's11',
             's12', 's13', 's14', 's15', 's16',
             's17', 's18', 's19', 's20', 's21', 
             's22')
'''

# ``bad subjects``  that should not be included in the analysis
exclude_subjects = {'subj01_noHPI'}

# Define the names of your ``runs``
# The naming should be consistant over subjects.
# put the number of runs you ideally expect to have per subject
# the scripts will issue a warning if there are less
# leave empty if there is just one file
runs = [''] # ['run01', 'run02']

# This generates the name for all files
# with the names specified above
# normally you should not have to touch this

base_fname = '{subject}_' + study_name + '{extension}.fif'

###############################################################################
# BAD CHANNELS
# ------------
#
# ``bad channels``, to be removed before maxfilter is applied
# you either get them from your recording notes, or from visualizing the data
# Use the simple dict if you don't have runs, and the dict(dict) if you have runs

# subj01, 'MEG2217'

bads = dict(s03=['MEG0213', 'MEG1932', 'MEG1923', 'MEG1442'])
            #s01=['MEG0213', 'MEG0731','MEG2211','MEG2411'])
            #s02=['MEG0213', 'MEG1422', 'MEG2141'],
            
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

# bads = dict(sample=dict(run01=['MEG 2443', 'EEG 053'],
#                         run02=['MEG 2443', 'EEG 053', 'EEG 013']))

###############################################################################
# DEFINE ADDITIONAL CHANNELS
# ------------
#
# Here you name/ replace  extra channels that were recorded, for instance EOG, ECG
# ``set_channel_types`` defines types of channels
# example : set_channel_types = {'EEG061': 'eog', 'EEG062': 'eog', 'EEG063': 'ecg', 'EEG064': 'misc'}
set_channel_types = {'EOG061': 'eog', 'EOG062': 'eog', 'ECG063': 'ecg', 'EMG064': 'emg'}

# ``rename_channels`` rename channels
# example : rename_channels = {'EEG061': 'EOG061', 'EEG062': 'EOG062', 'EEG063': 'ECG063'}
rename_channels = {}#{'EEG061': 'EOG061', 'EEG062': 'EOG062', 'EEG063': 'ECG063', 'EEG064': 'EMG064'}


###############################################################################
# FREQUENCY FILTERING
# -------------------
#
# ``h_freq``  : the high-frequency cut-off in the lowpass filtering step.
# Keep it None if no lowpass filtering should be applied.
h_freq = 40.

# ``l_freq``  : the low-frequency cut-off in the highpass filtering step.
# Keep it None if no highpass filtering should be applied.
l_freq = None


###############################################################################
# MAXFILTER PARAMETERS
# -------------------
#
# Download the ``cross talk file`` and ``calibration file`` (these are machine specific)
# path:
# and place them in the study folder
mf_ctc_fname = os.path.join(study_path, 'SSS', 'ct_sparse.fif')
mf_cal_fname = os.path.join(study_path, 'SSS', 'sss_cal.dat')

# ``mf_reference_run `` : defines the reference run used to adjust the head position for
# all other runs
mf_reference_run = 0  # take 1st run as reference for head position

# Set the origin for the head position
mf_head_origin = 'auto'

# ``mf_st_duration `` : if None, no temporal-spatial filtering is applied during MaxFilter,
# otherwise, put a float that speficifies the buffer duration in seconds,
# Elekta default = 10s, meaning it acts like a 0.1 Hz highpass filter
mf_st_duration = None


###############################################################################
# RESAMPLING
# ----------
#
# ``resample_sfreq``  : a float that specifies at which sampling frequency
# the data should be resampled. If None then no resampling will be done.
resample_sfreq = None


# ``decim`` : integer that says how much to decimate data at the epochs level.
# It is typically an alternative to the `resample_sfreq` parameter that
# can be used for resampling raw data. 1 means no decimation
decim = 1


###############################################################################
# AUTOMATIC REJECTION OF ARTIFACTS
# --------------------------------
#
#  ``reject`` : the default rejection limits to make some epochs as bads.
# This allows to remove strong transient artifacts.
# If you want to reject and retrieve blinks later, e.g. with ICA, don't specify
# a value for the eog channel (see examples below).
# **Note**: these numbers tend to vary between subjects.
# Examples:
# reject = {'grad': 4000e-13, 'mag': 4e-12, 'eog': 150e-6}
# reject = None

reject = {'grad': 4000e-13, 'mag': 4e-12, 'eeg': 200e-6}

###############################################################################
# EPOCHING
# --------
#
# ``tmin``: float that gives the start time before event of an epoch.
tmin = -3.

#  ``tmax`` : float that gives the end time after event of an epochs.
tmax = 1.

# ``baseline`` : tuple that specifies how to baseline the epochs; if None,
# no baseline is applied

baseline = (None, 0.)

# stimulus channel, which contains the events
stim_channel = None  # 'STI014'# 'STI101'

#  `event_id`` : python dictionary that maps events (trigger/marker values)
# to conditions. E.g. `event_id = {'Auditory/Left': 1, 'Auditory/Right': 2}`

event_id = {'2s': 2, '4s': 4, '8s': 8, '16s': 16, 'Inf': 32, 'Start': 1}
conditions = ['2s', '4s', '8s', '16s', 'Inf', 'Start']


###############################################################################
# ICA PARAMETERS
# --------------
# ``runica`` : boolean that says if ICA should be used or not.
runica = True

rejcomps_man = dict(sample=dict(meg=[],
                                eeg=[]))


###############################################################################
# DECODING
# --------------
#
# decoding_conditions should be a list of conditions to be classified.
# For example 'Auditory' vs. 'Visual' as well as
# 'Auditory/Left' vs 'Auditory/Right'
decoding_conditions = [('Auditory/Left', 'Auditory/Right'),
                       ('Auditory', 'Visual')]
decoding_metric = 'roc_auc'
decoding_n_splits = 5

###############################################################################
# TIME-FREQUENCY
# --------------
#
time_frequency_conditions = ['Auditory/Left']

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

random_state = 42
