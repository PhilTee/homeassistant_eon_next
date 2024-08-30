from homeassistant.core import HomeAssistant

DOMAIN = "eon_next"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up the integration from a config entry."""
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload a config entry."""
    return True