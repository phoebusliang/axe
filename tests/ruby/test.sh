#!/usr/bin/env bash
#clean old report
rm -fr report

mkdir -p report

bundle exec parallel_cucumber features -o '-t @complete-7p,@complete-6sp'

cd report && report_builder
