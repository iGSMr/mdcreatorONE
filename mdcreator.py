from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool

import os

from vizone.base import PayloadBase
from vizone.client import HTTPClientError, HTTPServerError, init
from vizone.vdf import Model
from vizone.payload.asset.item import Item
from vizone.payload.asset.itemcollection import ItemCollection
from vizone.payload.dictionary import Dictionary, DictionaryEntry
from vizone.resource.dictionary import get_dictionary_by_id
from vizone.payload.metadata.importexport import ImportExport
from vizone.resource.asset import create_asset, get_asset_by_id
from vizone.payload.metadata import MetadataFormCollection

from vizone.logging import log, close, info, error, xml, warn
from vizone.tool import Tool, encapsulate
from time import sleep
import datetime, time
from ftplib import FTP


__author__ = 'igi'

tool = Tool('migrationd')
tool.add_argument('-i', '--interval', type=int, default=600,
                  help='Unmanaged file refetch interval in seconds (default 600)')
tool.add_argument('--location', help='Storage handle to look for files in')
tool.add_argument('--form', help='Metadata form to use', default='hubitem')

args, client = tool.init()


def getmdform(param):
        try:
            mfc = MetadataFormCollection(client.GET("http://10.211.7.116/api/metadata/form?qType=" + param))
            for mfd in mfc.entries:
                print mfd.title
                print mfd.name

        except HTTPClientError:
            print("Error")

        return mfd


def getvdf(mfd):
    info("[mdcreatorcore]")

def main():
    # Get the unmanaged file location to monitor
    getmdform("ASSET.Item")
    getmdform("ASSET.ItemSet")
    getmdform("MEDIA.LogTrackItem")
    getmdform("COLLECTION.Collection.folder")
    getmdform("COLLECTION.Collection.series")
    getmdform("COLLECTION.Collection.season")
    getmdform("COLLECTION.Collection.program")
    # Listen for events on it


    #types.put("aggregate-asset", "ASSET.ItemSet");
    #types.put("logtrackitem", "MEDIA.LogTrackItem");
    #types.put("folder", "COLLECTION.Collection.folder");
    #types.put("series", "COLLECTION.Collection.series");
    #types.put("season", "COLLECTION.Collection.season");
    #types.put("program", "COLLECTION.Collection.program");
    #types.put("metadata-directory-entry", "METADATA.Directory");

    info("Started")

    interval_counter = 0

    try:
        while True:
            sleep(5)
            interval_counter += 5
            if interval_counter > args.interval:
                interval_counter = 0

    finally:
        # stomp.close()
        close()


tool.run(main)
