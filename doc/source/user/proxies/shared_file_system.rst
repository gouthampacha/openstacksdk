Shared File System API
======================

.. automodule:: openstack.shared_file_system.v2._proxy

The Shared File System Class
----------------------------

The accelerator high-level interface is available through the
``shared_file_system`` member of a :class:`~openstack.connection.Connection`
object. The ``shared_file_system`` member will only be added if the service is
detected.


Shared File System Availability Zones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interact with Availability Zones supported by the Shared File Systems
service.

.. autoclass:: openstack.shared_file_system.v2._proxy.Proxy
  :noindex:
  :members: list_availability_zones
