﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static DarkSoulsScripting.Hook;

namespace DarkSoulsScripting
{
    public class PCOptions : GameStruct
    {
        protected override void InitSubStructures()
        {

        }

        public int ScreenWidth
        {
            //Updated for DSR
            get { return RInt32(Address + 0xD0); }
            set { WInt32(Address + 0xD0, value); }
        }
        public int ScreenHeight
        {
            //Updated for DSR
            get { return RInt32(Address + 0xD0); }
            set { WInt32(Address + 0xD0, value); }
        }
    }
}