"""
Copyright 2022 Akamai Technologies, Inc. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from __future__ import annotations

from dataclasses import dataclass

from exceptions import setup_logger


logger = setup_logger()


@dataclass
class SingleHost:
    property_name: str
    contract_id: str
    product_id: str
    public_hostnames: list
    edge_hostname: str
    notification_emails: list

    group_id: str = ''
    edge_hostname_mode: str = 'use_existing_edgehostname'
    edge_hostname_id: int = 0

    # general
    secure_network: str = 'ENHANCED_TLS'
    rule_format: str = 'latest'
    create_new_cpcode: bool = True
    new_cpcode_name: str = ''
    version_notes: str = 'Initial Version'

    onboard_default_cpcode: int = 0
    onboard_property_id: str = ''

    # setup input files
    use_file: bool = True
    source_template_file: str = ''
    source_values_file: str = ''

    # pipeline
    use_folder: bool = False
    folder_path: str = ''
    env_name: str = ''

    use_existing_enrollment_id: bool = False
    existing_enrollment_id: int = 0
    create_new_ssl_cert: bool = False
    ssl_cert_template_file: str = ''
    ssl_cert_template_values: str = ''
    temp_existing_edge_hostname: str = 'xxx'

    # waf info
    waf_config_name: str = 'WAF Security File'
    create_new_security_config: bool = True
    add_selected_host: bool = True
    update_match_target: bool = True
    waf_match_target_id: str = ''
    onboard_waf_config_id: int = 0
    onboard_waf_prev_version: int = 0
    onboard_waf_config_version: int = 0
    policy_id: str = ''
    policy_name: str = 'Default'
    target_seq: int = 0
    target_id: int = 0

    # Staging activation
    activate_property_staging: bool = True
    activate_waf_policy_staging: bool = True

    # Production activation
    activate_property_production: bool = True
    activate_waf_policy_production: bool = True
