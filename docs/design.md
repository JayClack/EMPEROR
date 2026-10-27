# EMPEROR - Automated groundstation and radio monitoring system
## Introduction
### Purpose
This system will get TLE/OMM data for specific satellites, generate predictions on their passes based on local machine location, manage an SDR input stream, gather the data at the given time, store, and later decode the transmission, locally and automatically.

### Scope

### Definitions and Acronyms

### References

## System Overview
The system will consist of a number of individual modules, including orbital, sdr, groundstation, database, and possibly more.

The orbital module will be responsible for performing TLE/OMM gathering, orbital mechanics calculations, etc. The SDR module will be responsible for providing the interface with the SDR systems. The groundstation is the orchestrator, in that it will managing the general functions and database management, utilising the other modules. There will be a database module to provide the common interface for the database objects.

### System Description
The system is intended to track passes of particular orbital objects, enable an sdr dongle to retrieve radio emissions from said object, and record them with the goal of later decoding them to a useful file. Eventually as a P1 feature there will also be a web interface to allow general users to view the files, recorded objects, etc.

The groundstation module will have a scheduled task to fetch TLE/OMM data from celestrak for chosen tracked objects and generate pass files. The pass file will define the information required for tracking it, including key times for the pass, and potentially doppler frequencies for tracking it. 

A continuous service will check the pass predictions file, and sleep until a particular pass is near. During a pass the continuous service will operate the SDR to attempt to gather the radio emissions from the object, saving the data to file.

Later, a decryption system may be defined such that output files can be created as decryptions of the data being transmitted by the object. Careful consideration will be spent to ensure the object being tracked is a legal one.

### Design Goals
* Predict passes of satellite objects.
* Generate pass predictions for said objects.
* Retrieve radio emissions during a pass for said object.
* Store the data appropriately for future decryption.

## Architectural Design
### Data and Control Flow
The groundstation will be the primary driver of the process. Here will be defined the daily tasks, and also the daemon functions.

## Detailed Design

### Component Name

#### Responsibilities

#### Interfaces/APIs

#### Data Structures

#### Algorithms and Logic

#### State Management

## Database Design
### ER Diagram/Schema Diagram

### Tables and Collections

### Relationships

### Migration Strategy

## External Interfaces

### User Interface

### External APIs

### Hardware Interfaces

### Network Protocols and Communication

## Security
### Authentication

### Authorisation

### Data Protection

### Threat Model

## Performance and Scalability
### Expected Load

### Caching Strategy

### Database Optimisation

### Scaling Strategy

## Deployment Architecture
### Environments

### CI/CD Pipeline

### Infrastructure Diagram

### Cloud Hosting

### Containerisation/Orchestration

## Testing Strategy
### Unit Testing

### Integration Testing

### End-To-End Testing

### Quality Metrics

## Appendices