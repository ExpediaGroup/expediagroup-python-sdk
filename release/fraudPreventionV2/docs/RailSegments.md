[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [RailSegments](RailSegments.md)
# class `expediagroup.sdk.fraudpreventionv2.model.RailSegments`
```
RailSegments(
    departure_time: datetime,
    arrival_time: datetime,
    departure_station: RailwayStationDetails,
    arrival_station: RailwayStationDetails,
    transportation_method: TransportationMethod,
    operating_company: Optional[OperatingCompany],
)
```

pydantic model RailSegments



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    
        
    

|          Name         |                        Type                       | Required |                                                                                                                                                                                                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------|---------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    arrival_station    | [RailwayStationDetails](RailwayStationDetails.md) |   True   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      arrival_time     |                      datetime                     |   True   |                                                                                                                                                                                                                                                                                                                                                                                                 The local date and time of the scheduled arrival at the destination station, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                                                                                                                                                                                                                                                 |
|   departure_station   | [RailwayStationDetails](RailwayStationDetails.md) |   True   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     departure_time    |                      datetime                     |   True   |                                                                                                                                                                                                                                                                                                                                                                                                The local date and time of the scheduled departure from the departure station, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                                                                                                                                                                                                                                                |
|   operating_company   | Optional[[OperatingCompany](OperatingCompany.md)] |  False   |                                                                                                                                                                                                                                                                                                                                                                 This attribute captures the name or identifier of the company responsible for operating the Rail product. It represents the specific operating entity, such as Amtrak, British Railways, or a bus company.                                                                                                                                                                                                                                                                                                                                                                |
| transportation_method |  [TransportationMethod](TransportationMethod.md)  |   True   | This attribute represents the specific transportation method by which the passenger is traveling. It captures the mode of transportation used during the Rail product journey, Possible values are:<br/>    - `BUS` - The Rail product includes bus transportation for certain segments of the itinerary.<br/>    - `FERRY` - The Rail product involves ferry transportation as part of the journey.<br/>    - `PUBLIC_TRANSPORT` - The Rail product represents the use of public transportation modes for the journey.<br/>    - `TRAM` - The Rail product includes tram transportation as part of the journey.<br/>    - `RAIL` - The Rail product specifically utilizes train transportation for the journey.<br/>    - `TRANSFER` - The Rail product involves transfers between different modes of transportation.<br/>    - `OTHER` - The Rail product utilizes transportation methods not covered by the aforementioned categories. |










# Inheritance
object > BaseModel > RailSegments