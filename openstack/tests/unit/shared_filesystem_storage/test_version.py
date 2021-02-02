# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.shared_file_system import version
from openstack.tests.unit import base


IDENTIFIER = 'v2'
EXAMPLE = {
    'id': IDENTIFIER,
    'status': 'SUPPORTED',
    'version': '2.51',
    'min_version': '2.0',
    'updated': "2015-08-27T11:33:21Z",
    "links": [
        {
          "rel": "describedby",
          "type": "text/html",
          "href": "http://docs.openstack.org/"
        },
        {
          "rel": "self",
          "href": "http://10.0.110.111/v2/"
        }
      ],
}


class TestVersion(base.TestCase):

    def test_basic(self):
        version_resource = version.Version()
        self.assertEqual('version', version_resource.resource_key)
        self.assertEqual('versions', version_resource.resources_key)
        self.assertEqual('/', version_resource.base_path)
        self.assertIs(False, version_resource.allow_create)
        self.assertIs(False, version_resource.allow_fetch)
        self.assertIs(False, version_resource.allow_commit)
        self.assertIs(False, version_resource.allow_delete)
        self.assertIs(True, version_resource.allow_list)

    def test_make_version(self):
        version_resource = version.Version(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], version_resource.id)
        self.assertEqual(EXAMPLE['links'], version_resource.links)
        self.assertEqual(EXAMPLE['status'], version_resource.status)
        self.assertEqual(EXAMPLE['min_version'], version_resource.min_version)
        self.assertEqual(EXAMPLE['version'], version_resource.version)
        self.assertEqual(EXAMPLE['updated'], version_resource.updated)
