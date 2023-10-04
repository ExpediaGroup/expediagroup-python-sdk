[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [AirSegment](AirSegment.md)
# class `expediagroup.sdk.fraudpreventionv2.model.AirSegment`
```
AirSegment(
    airline_code: constr(max_length=10),
    departure_airport_code: constr(max_length=10),
    arrival_airport_code: constr(max_length=10),
    departure_time: Optional[datetime],
    arrival_time: Optional[datetime],
)
```

pydantic model AirSegment



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    

|          Name          |          Type         | Required |                                                      Description                                                       |
|------------------------|-----------------------|----------|------------------------------------------------------------------------------------------------------------------------|
|      airline_code      | constr(max_length=10) |   True   |                                            Airline code of the trip segment                                            |
|  arrival_airport_code  | constr(max_length=10) |   True   |                                          Arrival airport of the trip segment                                           |
|      arrival_time      |   Optional[datetime]  |  False   |  Local date and time of arrival to destination location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  |
| departure_airport_code | constr(max_length=10) |   True   |                                         Departure airport of the trip segment                                          |
|     departure_time     |   Optional[datetime]  |  False   | Local date and time of departure from departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |










# Inheritance
object > BaseModel > AirSegment