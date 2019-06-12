﻿using DarkSoulsScripting.Injection;
using System;
using System.Collections.Generic;

namespace DarkSoulsScripting
{   //"Map" = WorldChrMan
    public static class Map
    {
        //DSR 1.03
        public static IntPtr Address => Hook.RIntPtr((0x137D644, 0, 0x141D151B0));

        public static IntPtr PlayerPointer {
            //DSR
			get { return Hook.RIntPtr(Address + 0x68); }
            set { Hook.WIntPtr(Address + 0x68, value); }
		}

		public static int MapEntryCount {
            //DSR
			get { return Hook.RInt32(Address + 0xA0); }
		}

		public static List<MapEntry> GetEntries()
		{
            //DSR
            List<MapEntry> result = new List<MapEntry>();
			for (int i = 0; i < MapEntryCount; i++) {
                var addr = Hook.RIntPtr(Address + 0xA8 + (IntPtr.Size * i));
                result.Add(new MapEntry() { AddressReadFunc = () => addr });
			}
			return result;
		}

        public static MapEntry Find(int area, int block)
        {
            foreach (var e in GetEntries())
            {
                if (e.Area == (byte)area && e.Block == (byte)block)
                    return e;
            }

            return new MapEntry() { AddressReadFunc = () => IntPtr.Zero };
        }

        //TODO: REPLACE FUNCTION CALLS WITH DIRECT READS
        public static MapEntry GetCurrent()
        {
            return Find(IngameFuncs.GetCurrentMapAreaNo(), IngameFuncs.GetCurrentMapBlockNo());
        }
	}

}
