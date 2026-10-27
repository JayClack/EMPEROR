# Orbit Mean-Elements Message (OMM)

EMPEROR uses Orbit Mean-Elements Messages (OMMs) as the primary source of
orbital state data.

An OMM contains the mean orbital elements required to propagate an orbit
using models such as SGP4, together with metadata describing the tracked
space object.

Reference:
- CCSDS 502.0-B-3 Orbit Mean-Elements Message
- CelesTrak OMM documentation

---

# Orbital Elements

These parameters describe the shape, orientation, and current position
of an orbit.

## Mean Motion

Units: revolutions/day

The average number of orbital revolutions completed per day.

This value is used by orbit propagators to determine orbital period and
future spacecraft position.

A larger value corresponds to a lower orbit and shorter orbital period.

---

## Eccentricity

Units: dimensionless

Describes how circular or elliptical the orbit is.

- e = 0.0 → perfectly circular orbit
- 0 < e < 1 → elliptical orbit

Most operational satellites have relatively small eccentricities.

---

## Inclination

Units: degrees

The angle between the orbital plane and Earth's equatorial plane.

Examples:

- 0° → equatorial orbit
- 90° → polar orbit
- ~98° → sun-synchronous orbit

This determines the latitudes over which the spacecraft can pass.

---

## Right Ascension of the Ascending Node (RAAN)

Units: degrees

Defines the orientation of the orbital plane around Earth.

The ascending node is the point at which the spacecraft crosses the
equatorial plane travelling northward.

RAAN is the angle between:

1. The First Point of Aries (reference direction)
2. The ascending node

Measured in the equatorial plane.

Together with inclination, RAAN defines the orientation of the orbital
plane in three-dimensional space.

---

## Argument of Perigee

Units: degrees

Defines the orientation of the orbit within its orbital plane.

Specifically, it is the angle from:

1. The ascending node
2. The orbit's periapsis (closest approach to Earth)

Measured in the direction of motion.

For near-circular orbits this parameter becomes less physically useful,
since the periapsis location is poorly defined.

---

## Mean Anomaly

Units: degrees

Represents the spacecraft's position along its orbit at the specified
epoch.

Mean anomaly does not correspond directly to a physical angle measured
from Earth.

Instead, it is an angular parameter used by orbit propagators to
determine where the spacecraft was at the epoch and predict future
positions.

---

# Propagation Parameters

These terms are primarily used by the SGP4 orbit propagator.

## BSTAR

Units: inverse Earth radii

A drag term used by SGP4.

BSTAR approximates the effect of atmospheric drag on the spacecraft and
allows the propagator to model orbital decay.

This is particularly important for low Earth orbit satellites.

---

## Mean Motion First Derivative

Field: mean_motion_dot

Units: rev/day²

Rate of change of mean motion over time.

Provides information about long-term orbital evolution.

In modern SGP4 implementations this value is often not heavily utilised.

---

## Mean Motion Second Derivative

Field: mean_motion_ddot

Units: rev/day³

Second derivative of mean motion.

Represents acceleration of the mean motion change.

Usually very small and often ignored by modern propagators.

---

# Object Metadata

## Object Name

Human-readable spacecraft name.

Example:

- ISS (ZARYA)
- NOAA 19

---

## Object ID

International Designator.

Format:

YYYY-NNNPPP

Example:

1998-067A

Where:

- YYYY = launch year
- NNN = launch number
- PPP = payload identifier

---

## NORAD Catalogue Number

Unique identifier assigned by US Space Command.

Used as the primary key by many tracking services including CelesTrak.

---

## Classification

Space object classification.

Examples:

- U = Unclassified

---

## Element Set Number

Version number assigned to the orbital element set.

Used for tracking updates to the published orbit solution.

---

## Revolution Number at Epoch

The orbit count completed by the spacecraft at the epoch time.