from homeassistant import config_entries
from .const import DOMAIN

class EonNextConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Your Integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Your Integration", data=user_input)
        return self.async_show_form(step_id="user")