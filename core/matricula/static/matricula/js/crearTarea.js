var fvCrearTarea;

document.addEventListener('DOMContentLoaded', function (event) {
    const form = document.getElementById('frmCrearTarea');
    fvCrearTarea = FormValidation.formValidation(form, {
            locale: 'es_ES',
            localization: FormValidation.locales.es_ES,
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                submitButton: new FormValidation.plugins.SubmitButton(),
                // defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                bootstrap: new FormValidation.plugins.Bootstrap(),
                icon: new FormValidation.plugins.Icon({
                    valid: 'fa fa-check',
                    invalid: 'fa fa-times',
                    validating: 'fa fa-refresh',
                }),
            },

            fields: {
                name: {
                    validators: {
                        notEmpty: {
                            message: 'Llenar este campo..'
                        },
                        remote: {
                            url: pathname,
                            // Send { username: 'its value', email: 'its value' } to the back-end
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="name"]').value,
                                    type: 'name',
                                    action: 'validate_data'
                                };
                            },
                            message: 'El tema ya se encuentra registrado',
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
                juego: {
                    validators: {
                        notEmpty: {
                            message: 'Debe elegir un juego..'
                        },
                    }
                },

                
                
            }
            
        }
    )
        .on('core.element.validated', function (e) {
            if (e.valid) {
                const groupEle = FormValidation.utils.closest(e.element, '.form-group');
                if (groupEle) {
                    FormValidation.utils.classSet(groupEle, {
                        'has-success': false,
                    });
                }
                FormValidation.utils.classSet(e.element, {
                    'is-valid': false,
                });
            }
            const iconPlugin = fvCrearTarea.getPlugin('icon');
            const iconElement = iconPlugin && iconPlugin.icons.has(e.element) ? iconPlugin.icons.get(e.element) : null;
            iconElement && (iconElement.style.display = 'none');
        })
        .on('core.validator.validated', function (e) {
            if (!e.result.valid) {
                const messages = [].slice.call(form.querySelectorAll('[data-field="' + e.field + '"][data-validator]'));
                messages.forEach((messageEle) => {
                    const validator = messageEle.getAttribute('data-validator');
                    messageEle.style.display = validator === e.validator ? 'block' : 'none';
                });
            }
        })
        .on('core.form.valid', function () {
            var parameters = new FormData(fvCrearTarea.form);
            parameters.append('action', 'add_homework');
            let urlrefresh = fvCrearTarea.form.getAttribute('data-url');
            submit_formdata_with_ajax('Notificación',
                '¿Estas seguro de realizar la siguiente acción?',
                pathname,
                parameters,
                function (request) {
                    
                    location.href = urlrefresh;

                },
            );
        });
});


$(function () {

    $('.select2').select2({
        placeholder: 'Buscar..',
        language: 'es',
        theme: 'bootstrap4'
    });

    
});