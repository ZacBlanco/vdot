#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def duration_to_ms(duration):
  parts = str(duration).split(":")
  if len(parts) < 3:
    return duration
  h = int(parts[0])
  m = int(parts[1])
  parts = parts[2].split('.')
  s = int(parts[0])
  ms = int(parts[1])
  ret =  ms + (s * 1000) + (m * 1000 * 60) + (h * 60 * 60 * 1000)
  return ret


def main():
  df = pd.read_csv("./tables/races.csv")
  df = df.applymap(duration_to_ms)
  df.to_json("./tables/races.json")

  df = pd.read_csv("./tables/paces.csv")
  df = df.applymap(duration_to_ms)
  df.to_json("./tables/paces.json")


if __name__ == "__main__":
  main()
