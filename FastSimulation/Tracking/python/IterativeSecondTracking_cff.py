import FWCore.ParameterSet.Config as cms

from FastSimulation.Tracking.IterativeSecondSeedProducer_cff import *
from FastSimulation.Tracking.IterativeSecondCandidateProducer_cff import *
from FastSimulation.Tracking.IterativeSecondTrackProducer_cff import *
from FastSimulation.Tracking.IterativeSecondTrackMerger_cfi import *
from FastSimulation.Tracking.IterativeSecondTrackFilter_cff import *
iterativeSecondTracking = cms.Sequence(iterativeSecondSeeds+iterativeSecondTrackCandidatesWithTriplets+iterativeSecondTracks+iterativeSecondTrackMerging+iterativeSecondTrackFiltering)


