# Coral Bleaching Bayesian Analysis

Hierarchical Bayesian analysis of regional environmental predictors of coral bleaching severity using global reef survey data.

## Overview

This repository contains the code, cleaned dataset, figures, and capstone paper for a study examining how local environmental predictors influence coral bleaching severity across coral reef ecoregions.

The project applies hierarchical Bayesian beta regression to investigate whether the relationships between depth, turbidity, and windspeed vary regionally after accounting for thermal stress.

## Research Question

> To what extent do the effects of local environmental predictors on coral bleaching severity vary across ecoregions after accounting for thermal stress?

## Methods

The analysis uses:

- Hierarchical Bayesian beta regression
- Average marginal effects (AMEs)
- Markov Chain Monte Carlo (MCMC) estimation
- Bambi + NumPyro (NUTS sampler)

Environmental predictors examined:
- Depth
- Turbidity
- Windspeed

Control variable:
- Degree Heating Weeks (thermal stress)

## Dataset

The original coral bleaching dataset was compiled by:

van Woesik, R., & Burkepile, D. (2022)

BCO-DMO Coral Bleaching Dataset:
https://doi.org/10.26008/1912/bco-dmo.773466.2

## Author

Tom Unger
Bachelor Capstone Project
Amsterdam University College (AUC)
