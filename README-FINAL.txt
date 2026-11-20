Urban Sentinel - weather fallback release

Primary weather provider: Open-Meteo Forecast API.
Backup weather provider: Norwegian Meteorological Institute (MET Norway) Locationforecast 2.0 compact.
No API keys needed for this static website. Both sources report modelled 2-metre outdoor AIR temperature, not ground-surface temperature.
The browser sends its normal Origin header for MET Norway identification. MET Norway allows low-volume direct browser requests; higher-traffic deployments should use a caching backend/proxy and an identifying User-Agent.
MET Norway data: CC BY 4.0. Attribute the Norwegian Meteorological Institute (MET Norway) and do not imply endorsement.

On Open-Meteo errors, Home and City Intelligence automatically try MET Norway for current air temperature, humidity and wind. Precipitation is next-hour forecast from MET Norway; apparent temperature is not provided and is shown unavailable.
The Temperature Map uses Open-Meteo batch requests first. During outages it requests MET Norway backup for up to 12 cities per refresh to limit free API traffic. Selecting a city checks that city separately.
Last successful weather readings are cached in the visitor browser for up to 24 hours and marked as cached if shown after an outage. The site never fabricates values.
Historical temperature charts require Open-Meteo history; MET Norway forecast data cannot substitute for past observed weather.
AQI is still from Open-Meteo's air quality model, US AQI scale, not Indian CPCB AQI.
All 580 city selections and existing website pages remain; Intelligence Explorer remains removed.
Deploy this complete root-level ZIP to Netlify via drag and drop. The backup API requires the website to be served from a public HTTPS origin.
