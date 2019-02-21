# -*- coding: utf-8 -*-
from ScoutSuite.providers.base.configs.resource_config import ResourceConfig
from ScoutSuite.providers.aws.aws_facade import AwsFacade


class RegionsConfig(ResourceConfig):

    def __init__(self, service):
        self._service = service

    async def fetch_all(self, chosen_regions=None, partition_name='aws'):
        # TODO: Should be injected
        facade = AwsFacade()

        self['regions'] = {}
        for region in await facade.build_region_list(self._service, chosen_regions, partition_name):
            self['regions'][region] = {}
            
        self['regions_count'] = len(self['regions'])
