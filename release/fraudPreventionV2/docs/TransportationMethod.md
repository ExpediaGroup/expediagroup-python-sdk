[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [TransportationMethod](TransportationMethod.md)
# class `expediagroup.sdk.fraudpreventionv2.model.TransportationMethod`
```
TransportationMethod(
)
```

pydantic model TransportationMethod: This attribute represents the specific transportation method by which the passenger is traveling. It captures the mode of transportation used during the Rail product journey, Possible values are:
- `BUS` - The Rail product includes bus transportation for certain segments of the itinerary.
- `FERRY` - The Rail product involves ferry transportation as part of the journey.
- `PUBLIC_TRANSPORT` - The Rail product represents the use of public transportation modes for the journey.
- `TRAM` - The Rail product includes tram transportation as part of the journey.
- `RAIL` - The Rail product specifically utilizes train transportation for the journey.
- `TRANSFER` - The Rail product involves transfers between different modes of transportation.
- `OTHER` - The Rail product utilizes transportation methods not covered by the aforementioned categories.



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    

|       Name       | Type | Required | Description |
|------------------|------|----------|-------------|
|       BUS        | Any  |   True   |     ...     |
|      FERRY       | Any  |   True   |     ...     |
|      OTHERS      | Any  |   True   |     ...     |
| PUBLIC_TRANSPORT | Any  |   True   |     ...     |
|       RAIL       | Any  |   True   |     ...     |
|       TRAM       | Any  |   True   |     ...     |
|     TRANSFER     | Any  |   True   |     ...     |










# Inheritance
object > Enum > TransportationMethod