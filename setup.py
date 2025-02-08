from cx_Freeze import setup,Executable,sys
includefiles=['bill.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "RetailBillingSystem",
     "TARGETDIR",
     "[TARGETDIR]\RetailSystem.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Billing System",
    author="Aniket Sonawane",
    name="Billing System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="RetailSystem.py",
            base=base,
            icon='bill.ico',
        )
    ]
)