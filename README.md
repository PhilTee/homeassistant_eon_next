## Get the Account Balance Only
```bash
curl 'https://api.eonnext-kraken.energy/v1/graphql/' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en;q=0.9' \
  -H 'authorization: JWTPLACEHOLDER' \
  -H 'content-type: application/json' \
  --data-raw $'{ "operationName": "GetOptimizelyAttributeUserData", "variables": { "accountNumber": "A-CC0UN7-NUM83R" }, "query": "query GetOptimizelyAttributeUserData($accountNumber: String!) {\\n      account(accountNumber: $accountNumber) {balance}}"}'
```

### Get Meter Readings
```bash
curl 'https://api.eonnext-kraken.energy/v1/graphql/' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en;q=0.9' \
  -H 'authorization: JWTPLACEHOLDER' \
  -H 'content-type: application/json' \
  --data-raw $'{"operationName":"getAccountMeterSelector","variables":{"accountNumber":"A-CC0UN7-NUM83R","showInactive":true},"query":"query getAccountMeterSelector($accountNumber: String!, $showInactive: Boolean!) {\\n  properties(accountNumber: $accountNumber) {\\n    ...MeterSelectorPropertyFields\\n    __typename\\n  }\\n}\\n\\nfragment MeterSelectorPropertyFields on PropertyType {\\n  __typename\\n  electricityMeterPoints {\\n    ...MeterSelectorElectricityMeterPointFields\\n    __typename\\n  }\\n  gasMeterPoints {\\n    ...MeterSelectorGasMeterPointFields\\n    __typename\\n  }\\n  id\\n  postcode\\n}\\n\\nfragment MeterSelectorElectricityMeterPointFields on ElectricityMeterPointType {\\n  __typename\\n  id\\n  meters(includeInactive: $showInactive) {\\n    ...MeterSelectorElectricityMeterFields\\n    __typename\\n  }\\n}\\n\\nfragment MeterSelectorElectricityMeterFields on ElectricityMeterType {\\n  __typename\\n  activeTo\\n  id\\n  registers {\\n    id\\n    name\\n    __typename\\n  }\\n  readings(first: 100) {\\n    edges {\\n      node {\\n        id\\n        readAt\\n        source\\n        registers {\\n          isQuarantined\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  serialNumber\\n}\\n\\nfragment MeterSelectorGasMeterPointFields on GasMeterPointType {\\n  __typename\\n  id\\n  meters(includeInactive: $showInactive) {\\n    ...MeterSelectorGasMeterFields\\n    __typename\\n  }\\n}\\n\\nfragment MeterSelectorGasMeterFields on GasMeterType {\\n  __typename\\n  activeTo\\n  id\\n  registers {\\n    id\\n    name\\n    __typename\\n  }\\n  readings(first: 100) {\\n    edges {\\n      node {\\n        id\\n        readAt\\n        source\\n        registers {\\n          isQuarantined\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  serialNumber\\n}\\n"}'
  ```

## TODO
- [ ] Setup basic HomeAssistant Integration Structure
- [ ] Implement the Account Balance API call
- [ ] Create the Account Balance Sensor Entity
- [ ] Add configuration to configuration.yml
- [ ] Implement the Login mutation call to get the JWT
- [ ] Determine if the GetOptimizelyAttributeUserData and the getAccountMeterSelector queries can be fetched ina single GQL API call
- [ ] Get meter readings from getAccountMeterSelector query
- [ ] Create Sensor Entities for:
  - [ ] Electricity Day Reading
  - [ ] Electricity Night Reading 
  - [ ] Electricity Reading Date
  - [ ] Electricity Reading Type
  - [ ] Gas Reading 
  - [ ] Gas Reading Date
  - [ ] Gas Reading Type