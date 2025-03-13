
from const.Const_Parameter import *

from system.UI.UI_PyToExe import *
from system.Loader_Pyinstaller_Struct import *
from system.UI.Dialog_Multi_Info import *
from system.UI.Dialog_Single_Info import *
from system.UI.Dialog_State_Info import *
from system.Thread_Pack_Launcher import *

import shutil


_log = Log.UI


class FunctionUI(PyToExeUI):
    def __init__(self):
        super().__init__()
        self.init_python_file_path()
        self.flag_initialized = True

    def init_parameters(self):
        super().init_parameters()
        self.dict_functions: dict = {
            # ===================================================== [主页] =====================================================
            'python_file_path': self.set_input_py_file_path_from_browser,
            'output_folder_path': self.set_output_folder_path_from_browser,
            'output_file_name': functools.partial(self.to_page, 0),
            'output_method': functools.partial(self.to_page, 0),
            'contents_directory': self.add_contents_directory,
            'console_window_control': functools.partial(self.to_page, 0),
            'add_icon': self.add_icon,
            'version_file': self.set_version_file_path_from_button,
            # ===================================================== [通用] =====================================================
            'add_file_folder_data': self.add_file_folder_data,
            'add_binary_data': self.add_binary_data,
            'collect_submodules': self.add_collect_submodules,
            'collect_data': self.add_collect_data,
            'collect_binaries': self.add_collect_binaries,
            'collect_all': self.add_collect_all,
            'hidden_imports': self.add_hidden_import,
            'import_paths': self.add_import_path,
            'exclude_module': self.add_exclude_module,
            'copy_metadata': self.add_copy_metadata,
            'recursive_copy_metadata': self.add_recursive_copy_metadata,
            'additional_hooks_dir': self.add_additional_hooks_dir,
            'runtime_hook': self.add_runtime_hook,
            'upx_exclude': self.add_upx_exclude,
            'add_splash_screen': self.add_splash_screen,
            'runtime_tmpdir': self.add_runtime_tmpdir,
            'workpath_option': self.add_workpath_option,
            'specpath': self.add_specpath,
            'upx_dir': self.add_upx_dir,
            'log_level': self.add_log_level,
            'python_option': self.add_python_option,
            'debug_mode': self.add_debug_mode,
            'optimize_level': self.add_optimize_level,
            'noupx_option': functools.partial(self.to_page, 1),  # ComboBox
            'disable_traceback': functools.partial(self.to_page, 1),  # ComboBox
            'ignore_signals': functools.partial(self.to_page, 1),  # ComboBox
            'noconfirm_option': functools.partial(self.to_page, 1),  # ComboBox
            'strip_option': functools.partial(self.to_page, 1),  # ComboBox
            'clean_cache': functools.partial(self.to_page, 1),  # ComboBox
            # ===================================================== [IOS/ Win] =====================================================
            'add_resource': self.add_resource,
            'codesign_identity': self.add_codesign_identity,
            'osx_bundle_identifier': self.add_osx_bundle_identifier,
            'osx_entitlements_file': self.add_osx_entitlements_file,
            'add_xml_file': self.add_xml_file,
            'hide_console': self.add_hide_console,
            'target_architecture': functools.partial(self.to_page, 2),  # ComboBox
            'argv_emulation': functools.partial(self.to_page, 2),  # ComboBox
            'uac_admin_apply': functools.partial(self.to_page, 2),  # ComboBox
            'uac_uiaccess': functools.partial(self.to_page, 2),  # ComboBox
        }

    def init_ui(self):
        super().init_ui()

    def init_signal_connections(self):
        super().init_signal_connections()
        # ===================================================== [主页] =====================================================
        self.pb_input_py_file_browser.clicked.connect(self.set_input_py_file_path_from_browser)
        self.pb_output_folder_browser.clicked.connect(self.set_output_folder_path_from_browser)
        self.pb_output_exe_version_browser.clicked.connect(self.set_version_file_path_from_button)
        self.pb_output_exe_version_edit.clicked.connect(self.edit_version_file)
        self.pb_output_exe_icon_browser.clicked.connect(self.add_icon)
        self.pb_contents_directory.clicked.connect(self.add_contents_directory)
        self.le_input_py_file_path.editingFinished.connect(self.set_input_py_file_path_from_lineEdit)
        self.le_output_folder_path.editingFinished.connect(self.set_output_folder_path_from_lineEdit)
        self.le_output_file_name.editingFinished.connect(self.set_output_file_name)
        self.le_output_exe_version.editingFinished.connect(self.set_version_file_path_from_lineEdit)
        self.rb_output_as_file.toggled.connect(self.add_output_exe_method)
        self.rb_output_as_folder.toggled.connect(self.add_output_exe_method)
        self.rb_exe_console_display_hide.toggled.connect(self.add_console_display_state)
        self.rb_exe_console_display_show.toggled.connect(self.add_console_display_state)
        self.pb_launch.clicked.connect(self.launch_packing)
        # ===================================================== [通用] =====================================================
        self.pb_add_file_folder_data.clicked.connect(self.add_file_folder_data)
        self.pb_add_binary_data.clicked.connect(self.add_binary_data)
        self.pb_collect_submodules.clicked.connect(self.add_collect_submodules)
        self.pb_collect_data.clicked.connect(self.add_collect_data)
        self.pb_collect_binaries.clicked.connect(self.add_collect_binaries)
        self.pb_collect_all.clicked.connect(self.add_collect_all)
        self.pb_hidden_imports.clicked.connect(self.add_hidden_import)
        self.pb_import_paths.clicked.connect(self.add_import_path)
        self.pb_exclude_module.clicked.connect(self.add_exclude_module)
        self.pb_copy_metadata.clicked.connect(self.add_copy_metadata)
        self.pb_recursive_copy_metadata.clicked.connect(self.add_recursive_copy_metadata)
        self.pb_additional_hooks_dir.clicked.connect(self.add_additional_hooks_dir)
        self.pb_runtime_hook.clicked.connect(self.add_runtime_hook)
        self.pb_upx_exclude.clicked.connect(self.add_upx_exclude)
        self.pb_add_splash_screen.clicked.connect(self.add_splash_screen)
        self.pb_runtime_tmpdir.clicked.connect(self.add_runtime_tmpdir)
        self.pb_workpath_option.clicked.connect(self.add_workpath_option)
        self.pb_specpath.clicked.connect(self.add_specpath)
        self.pb_upx_dir.clicked.connect(self.add_upx_dir)
        self.pb_log_level.clicked.connect(self.add_log_level)
        self.pb_python_option.clicked.connect(self.add_python_option)
        self.pb_debug_mode.clicked.connect(self.add_debug_mode)
        self.pb_optimize_level.clicked.connect(self.add_optimize_level)
        self.cb_noupx_option.stateChanged.connect(self.add_noupx_option)
        self.cb_disable_traceback.stateChanged.connect(self.add_disable_traceback)
        self.cb_ignore_signals.stateChanged.connect(self.add_ignore_signals)
        self.cb_noconfirm_option.stateChanged.connect(self.add_noconfirm_option)
        self.cb_strip_option.stateChanged.connect(self.add_strip_option)
        self.cb_clean_cache.stateChanged.connect(self.add_clean_cache)
        # ===================================================== [IOS/ Win] =====================================================
        self.pb_add_resource.clicked.connect(self.add_resource)
        self.pb_codesign_identity.clicked.connect(self.add_codesign_identity)
        self.pb_osx_bundle_identifier.clicked.connect(self.add_osx_bundle_identifier)
        self.pb_osx_entitlements_file.clicked.connect(self.add_osx_entitlements_file)
        self.pb_add_xml_file.clicked.connect(self.add_xml_file)
        self.pb_target_architecture.clicked.connect(self.add_target_architecture)
        self.pb_hide_console.clicked.connect(self.add_hide_console)
        self.cb_argv_emulation.stateChanged.connect(self.add_argv_emulation)
        self.cb_uac_admin_apply.stateChanged.connect(self.add_uac_admin_apply)
        self.cb_uac_uiaccess.stateChanged.connect(self.add_uac_uiaccess)

    def launch_packing(self):
        # STYLE.getProperty('$btn_svg_color').set_value('#00ff00')
        # STYLE.getProperty('$btn_svg_color_in_2').set_value(('#00ff00', '#ff00ff'))
        # return
        self.__shouldRemoveSplashModuleFile = False
        self.__splash_module_file_path = ''
        # 检查是否存在要打包的文件
        if not os.path.exists(self.data_manager.pyinstaller_struct.python_file_path.command_args):
            DialogMessageBox.error(self, LM.getWord('error_no_file_to_pack'))
            return
        # 检查输出方式, 输出路径, 控制台显示
        if not self.data_manager.pyinstaller_struct.python_file_path.command_args.endswith('.spec'):
            self.check_default_parameters()
        # 定位到输出信息页面
        if not 2 < self.stackedWidget.currentIndex() < 6:
            self.to_page(3)
            DialogMessageBox.info(self, LM.getWord('info_check_before_packing'))
            return

        # 选择打包方式
        if self.rb_env_builtin.isChecked():
            self.data_manager.pyinstaller_struct.optimize_level.clear_args()
            cmd = self.data_manager.pyinstaller_struct.get_command_list(self.rb_output_as_folder.isChecked())
        else:
            if self.rb_use_python.isChecked() and self.data_manager.current_env.pyinstaller_path:
                cmd = self.data_manager.command_use_python()
                cmd = cmd.replace('\n', '&&')
            elif self.rb_use_pyinstaller.isChecked() and self.data_manager.current_env.pyinstaller_path:
                cmd = self.data_manager.command_use_pyinstaller()
                cmd = cmd.replace('\n', '&&')
            else:
                res = DialogMessageBox.info(self, LM.getWord('no_pyinstaller_use_builtin'))
                if res == DialogMessageBox.StandardButton.CANCEL:
                    return
                self.data_manager.pyinstaller_struct.optimize_level.clear_args()
                cmd = self.data_manager.pyinstaller_struct.get_command_list(self.rb_output_as_folder.isChecked())
        index_auto_add_version = self.cbb_auto_add_version.currentData()
        # 检查是否需要添加版本号
        if index_auto_add_version >= 0:
            VersionEditor.add_version(self, self.le_output_exe_version.text(), index_auto_add_version)
            pass
        # 检查是否需要处理启动画面相关文件
        if self.cb_splash_auto_file_handle.isChecked() and self.data_manager.pyinstaller_struct.add_splash_screen.command_args:
            _log.info('处理启动画面相关文件')
            self.handle_splash_screen_reference()
        # 启动打包线程
        if not hasattr(self, 'launch_process'):
            self.launch_process = ThreadPackLauncher(self)
            self.launch_process.signal_cmd_text.connect(self.__read_process_output)
            self.launch_process.signal_thread_finished.connect(self.__on_packing_finished)
            self.launch_process.signal_processbar_value.connect(self.progressBar.setValue)
            self.pb_launch_cancel.clicked.connect(self.launch_process.stop)
        self.launch_process.set_cmd(cmd)
        self.pb_launch.hide()
        self.wdg_progressbar.show()
        if isinstance(cmd, str):
            self.pb_launch_cancel.show()
        self.launch_process.start()

    def check_default_parameters(self) -> None:
        if 'output_method' not in self.data_manager.pyinstaller_struct.get_command_dict(self.rb_output_as_folder.isChecked()):
            self.add_output_exe_method()
        if 'console_window_control' not in self.data_manager.pyinstaller_struct.get_command_dict(self.rb_output_as_folder.isChecked()):
            self.add_console_display_state()
        if 'output_folder_path' not in self.data_manager.pyinstaller_struct.get_command_dict(self.rb_output_as_folder.isChecked()):
            struct = self.data_manager.pyinstaller_struct.output_folder_path
            output_path = os.path.dirname(self.data_manager.pyinstaller_struct.python_file_path.command_args)
            struct.set_args(output_path)

    def handle_splash_screen_reference(self) -> None:
        file_path: str = self.data_manager.pyinstaller_struct.python_file_path.command_args
        _log.info('file_path: %s', file_path, file_path.endswith(('.py', '.pyw')))
        if not file_path.endswith(('.py', '.pyw')):
            return
        self.__splash_module_file_path = os.path.join(os.path.dirname(file_path), 'SplashModule.py')
        __rewrite = False
        with open(file_path, 'r', encoding='utf-8') as file:
            self.__main_file_original_list = file.readlines()
            # 判断是否已写过import SplashModule
            if 'import SplashModule\n' not in self.__main_file_original_list:
                __rewrite = True
        if __rewrite:
            # 在主文件中插入'import SplashModule\n'
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('import SplashModule\n')
                file.writelines(self.__main_file_original_list)
        # 写入SplashModule
        with open(self.__splash_module_file_path, 'w', encoding='utf-8') as file:
            file.write("""\
from contextlib import suppress
with suppress(ModuleNotFoundError):
    import pyi_splash
    pyi_splash.close()
""")
        self.__shouldRemoveSplashModuleFile = True

    def __read_process_output(self, data):
        if data:
            self.tb_console.append_text(data)

    def __on_packing_finished(self, flag: bool) -> None:
        _log.info('--------------------'+LM.getWord('info_packing_finished')+'--------------------')
        self.pb_launch.show()
        self.pb_launch_cancel.hide()
        self.wdg_progressbar.hide()
        self.delete_files_after_packing(flag)

    def delete_files_after_packing(self, flag: bool) -> None:
        if self.cb_delete_build.isChecked() or not flag:
            path = self.data_manager.pyinstaller_struct.output_folder_path.command_args
            dist_path = os.path.join(path, 'dist')
            build_path = os.path.join(path, 'build')
            try:
                if os.path.exists(dist_path):
                    # _log.error(dist_path)
                    shutil.move(dist_path, path)
                    shutil.rmtree(dist_path)
                # _log.error(build_path)
                shutil.rmtree(build_path)
            except FileNotFoundError:
                pass
            except Exception as e:
                _log.exception()
        if self.cb_delete_spec.isChecked() or not flag:
            path = self.data_manager.pyinstaller_struct.specpath.command_args
            if not path:
                path = self.data_manager.pyinstaller_struct.output_folder_path.command_args
            if not path:
                path = os.path.dirname(self.data_manager.pyinstaller_struct.python_file_path.command_args)
            spec_path = os.path.join(path, f'{self.data_manager.pyinstaller_struct.output_file_name.command_args}.spec')
            try:
                os.remove(spec_path)
            except FileNotFoundError:
                pass
            except Exception as e:
                _log.exception()
        if self.__shouldRemoveSplashModuleFile:
            with open(self.data_manager.pyinstaller_struct.python_file_path.command_args, 'w', encoding='utf-8') as file:
                file.writelines(self.__main_file_original_list)
            try:
                if os.path.exists(self.__splash_module_file_path):
                    os.remove(self.__splash_module_file_path)
            except:
                pass

    # ===================================================== [主页] =====================================================

    def init_python_file_path(self):
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            self.app_workspace_path = os.path.dirname(file_path)
            self.set_input_file(file_path)
        else:
            self.load_pyinstaller_command(SM.getConfig('pyinstaller_command'))

    def set_input_py_file_path_from_lineEdit(self):
        file_path: str = self.le_input_py_file_path.text()
        self.set_input_file(file_path)

    def set_input_py_file_path_from_browser(self):
        accept_files_type = LM.getWord('accept_files_type')
        file_path = QFileDialog.getOpenFileName(
            self, LM.getWord('select_input_file'), '', f"""{accept_files_type} (*.py *.pyw *.pyd *.spec *.txt);; 
            Python Files (*.py *.pyw *.pyd *.spec);; 
            Text Files (*.txt)""")[0]
        if not file_path:
            return
        self.set_input_file(file_path)

    def set_output_folder_path_from_browser(self):
        folder_path = QFileDialog.getExistingDirectory(self, LM.getWord('question_select_output_folder'), self.app_workspace_path)
        if not folder_path:
            return
        self.installer.output_folder_path.set_args(folder_path)

    def set_output_folder_path_from_lineEdit(self):
        folder_path = self.le_output_folder_path.text()
        if not folder_path:
            return
        self.installer.output_folder_path.set_args(folder_path)

    def set_output_file_name(self):
        file_name: str = self.le_output_file_name.text()
        if not file_name:
            return
        self.installer.output_file_name.set_args(file_name)

    def set_version_file_path_from_button(self):
        version_hint_text = LM.getWord('version_file')
        file_path: str = QFileDialog.getOpenFileName(self, LM.getWord('question_select_version_file'), '', f'{version_hint_text} (*.txt)')[0]
        if not file_path:
            return
        self.installer.version_file.set_args(file_path)

    def set_version_file_path_from_lineEdit(self):
        file_path: str = self.le_output_exe_version.text()
        if not file_path or not os.path.exists(file_path):
            return
        self.installer.version_file.set_args(file_path)

    def edit_version_file(self):
        file_path: str = self.le_output_exe_version.text()
        version_file_path: str = VersionEditor.edit(self, file_path)
        if version_file_path and file_path != version_file_path:
            self.le_output_exe_version.setText(version_file_path)

    def add_icon(self):  # 文件路径
        struct: MultiInfoStruct = self.installer.add_icon
        DialogMultiAbsolutePath.edit(self, struct, data_type='file')

    def add_contents_directory(self):  # 文件夹路径
        struct: SingleInfoStruct = self.installer.contents_directory
        DialogSingleInfo.edit(self, struct, data_type='text')

    def add_output_exe_method(self):
        struct: StateStruct = self.installer.output_method
        if self.rb_output_as_file.isChecked():
            struct.set_state('--onefile')
        else:
            struct.set_state('--onedir')

    def add_console_display_state(self):
        struct: StateStruct = self.installer.console_window_control
        if self.rb_exe_console_display_show.isChecked():
            struct.set_state('--console')
        else:
            struct.set_state('--noconsole')

            # ===================================================== [通用] =====================================================

    def add_file_folder_data(self):
        struct: RelPathStruct = self.installer.add_file_folder_data
        DialogMultiRelativePath.edit(self, struct)

    def add_binary_data(self):
        struct: RelPathStruct = self.installer.add_binary_data
        DialogMultiRelativePath.edit(self, struct)

    def add_collect_submodules(self):  # 模块名称 或 文件夹路径
        struct: MultiInfoStruct = self.installer.collect_submodules
        DialogMultiArgs.edit(self, struct, data_type='folder')

    def add_collect_data(self):  # 文件路径 或 文件夹路径
        struct: MultiInfoStruct = self.installer.collect_data
        DialogMultiAbsolutePath.edit(self, struct)

    def add_collect_binaries(self):  # 文件路径 或 文件夹路径
        struct: MultiInfoStruct = self.installer.collect_binaries
        DialogMultiAbsolutePath.edit(self, struct)

    def add_collect_all(self):  # 模块名称
        struct: MultiInfoStruct = self.installer.collect_all
        DialogMultiArgs.edit(self, struct)

    def add_hidden_import(self):  # 模块名称
        struct: MultiInfoStruct = self.installer.hidden_imports
        DialogMultiArgs.edit(self, struct)

    def add_import_path(self):  # 文件夹路径
        struct: MultiInfoStruct = self.installer.import_paths
        DialogMultiAbsolutePath.edit(self, struct, data_type='folder')

    def add_exclude_module(self):  # 模块名称
        struct: MultiInfoStruct = self.installer.exclude_module
        DialogMultiArgs.edit(self, struct)

    def add_copy_metadata(self):  # 模块名称
        struct: MultiInfoStruct = self.installer.copy_metadata
        DialogMultiArgs.edit(self, struct)

    def add_recursive_copy_metadata(self):  # 模块名称
        struct: MultiInfoStruct = self.installer.recursive_copy_metadata
        DialogMultiArgs.edit(self, struct)

    def add_additional_hooks_dir(self):  # 文件夹路径
        struct: MultiInfoStruct = self.installer.additional_hooks_dir
        DialogMultiAbsolutePath.edit(self, struct, data_type='folder')

    def add_runtime_hook(self):  # 文件路径
        struct: MultiInfoStruct = self.installer.runtime_hook
        DialogMultiAbsolutePath.edit(self, struct, data_type='file')

    def add_upx_exclude(self):  # 模块名称 或 文件路径
        struct: MultiInfoStruct = self.installer.upx_exclude
        DialogMultiArgs.edit(self, struct, data_type='file')

    def add_splash_screen(self):
        struct: SingleInfoStruct = self.installer.add_splash_screen
        pic_text = LM.getWord('image')
        DialogSingleInfo.edit(self, struct, data_type='file', accept_file=f'PNG {pic_text} (*.png);;')

    def add_runtime_tmpdir(self):
        struct: SingleInfoStruct = self.installer.runtime_tmpdir
        DialogSingleInfo.edit(self, struct, data_type='folder')

    def add_workpath_option(self):
        struct: SingleInfoStruct = self.installer.workpath_option
        DialogSingleInfo.edit(self, struct, data_type='folder')

    def add_specpath(self):
        struct: SingleInfoStruct = self.installer.specpath
        DialogSingleInfo.edit(self, struct, data_type='folder')

    def add_upx_dir(self):
        struct: SingleInfoStruct = self.installer.upx_dir
        DialogSingleInfo.edit(self, struct, data_type='folder')

    def add_log_level(self):
        struct: StateStruct = self.installer.log_level
        DialogStateInfo.edit(self, struct)

    def add_python_option(self):
        struct: StateStruct = self.installer.python_option
        DialogStateInfo.edit(self, struct, withHash=True)

    def add_debug_mode(self):
        struct: StateStruct = self.installer.debug_mode
        DialogStateInfo.edit(self, struct)

    def add_optimize_level(self):
        struct: StateStruct = self.installer.optimize_level
        DialogStateInfo.edit(self, struct)

    def add_noupx_option(self):
        struct: SwitchStruct = self.installer.noupx_option
        if self.cb_noupx_option.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_disable_traceback(self):
        struct: SwitchStruct = self.installer.disable_traceback
        if self.cb_disable_traceback.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_ignore_signals(self):
        struct: SwitchStruct = self.installer.ignore_signals
        if self.cb_ignore_signals.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_noconfirm_option(self):
        struct: SwitchStruct = self.installer.noconfirm_option
        if self.cb_noconfirm_option.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_strip_option(self):
        struct: SwitchStruct = self.installer.strip_option
        if self.cb_strip_option.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_clean_cache(self):
        struct: SwitchStruct = self.installer.clean_cache
        if self.cb_clean_cache.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    # ===================================================== [IOS/ Win] =====================================================
    def add_resource(self):  # 文件路径
        struct: MultiInfoStruct = self.installer.add_resource
        DialogMultiResourcePath.edit(self, struct)

    def add_codesign_identity(self):
        struct: SingleInfoStruct = self.installer.codesign_identity
        DialogSingleInfo.edit(self, struct, data_type='text')

    def add_osx_bundle_identifier(self):
        struct: SingleInfoStruct = self.installer.osx_bundle_identifier
        DialogSingleInfo.edit(self, struct, data_type='text')

    def add_osx_entitlements_file(self):
        struct: SingleInfoStruct = self.installer.osx_entitlements_file
        DialogSingleInfo.edit(self, struct, data_type='file')

    def add_xml_file(self):
        struct: SingleInfoStruct = self.installer.add_xml_file
        DialogSingleInfo.edit(self, struct, data_type='file')

    def add_hide_console(self):
        struct: StateStruct = self.installer.hide_console
        DialogStateInfo.edit(self, struct)

    def add_target_architecture(self):
        struct: StateStruct = self.installer.target_architecture
        DialogStateInfo.edit(self, struct)

    def add_argv_emulation(self):
        struct: SwitchStruct = self.installer.argv_emulation
        if self.cb_argv_emulation.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_uac_admin_apply(self):
        struct: SwitchStruct = self.installer.uac_admin_apply
        if self.cb_uac_admin_apply.isChecked():
            struct.set_on()
        else:
            struct.set_off()

    def add_uac_uiaccess(self):
        struct: SwitchStruct = self.installer.uac_uiaccess
        if self.cb_uac_uiaccess.isChecked():
            struct.set_on()
        else:
            struct.set_off()
