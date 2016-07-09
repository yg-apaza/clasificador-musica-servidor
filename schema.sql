drop if exists songs;
create table songs(
    id integer primary key autoincrement,
    nombre text not null,
    url text not null,
    data text not null,
    meanCentroid real not null,
    meanRollOff real not null,
    meanFlux real not null,
    meanZeroCrossings real not null,
    stdCentroid real not null,
    stdRollOff real not null,
    stdFlux real not null,
    stdZeroCrossings real not null,
    lowEnergy real not null,
    period0 real not null,
    amplitude0 real not null,
    radioPeriod1  real not null,
    amplitude1  real not null,
    ratioPeriod2  real not null,
    amplitude2  real not null,
    ratioPeriod3  real not null,
    amplitude3  real not null
);
