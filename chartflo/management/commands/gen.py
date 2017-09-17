# -*- coding: utf-8 -*-

from __future__ import print_function
from django.core.management.base import BaseCommand
from chartflo.apps import GENERATORS
from goerr import err
from .gencharts import get_changes_events, get_last_run_q, get_events_q
from mqueue.models import MEvent


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument('app', type=str)
        parser.add_argument('-q',
                            dest="quiet",
                            default=0,
                            help='Quiet mode: ex: -q=1',
                            )
        parser.add_argument('-all',
                            dest="all",
                            default=0,
                            help='Update for all instances: ex: -all=1',
                            )

    def handle(self, *args, **options):
        """
        Run a generator
        """
        app = options["app"]
        quiet = int(options["quiet"])
        runall = int(options["all"])
        try:
            generator = GENERATORS[app]
        except Exception as e:
            err.new(e, "Generator not found")
            if quiet > 0:
                print("Generator not found")
            return
        if quiet > 0:
            print("Running generator", app)
        try:
            last_run_q = get_last_run_q()
        except Exception as e:
            err.new(e)
        if runall == 0:
            try:
                events_q = get_events_q()
            except Exception as e:
                err.new(e)
            try:
                events_q = get_changes_events(events_q, last_run_q)
            except Exception as e:
                err.new(e)
        else:
            try:
                events_q = MEvent.objects.all()
            except Exception as e:
                err.new(e)
        try:
            generator(events_q)
        except Exception as e:
            err.new(e)
        if err.exists:
            err.throw()