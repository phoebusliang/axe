#!/usr/bin/env bash
#clean old report
rm -fr report

mkdir -p report

bundle exec parallel_cucumber features -o '-t @complete-hp'

cd report && report_builder
