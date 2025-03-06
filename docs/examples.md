# Forge API

### Setup

```permission_name: str``` *Permission Name*

```permission: str``` *Permission*

```python
from forge.api import Forge
from forge.permissions import Role

instance = Forge()

# My roles
admin_role = Role('Admin', ['role.admin'])

# Add role
instance.add_role(admin_role)

```
