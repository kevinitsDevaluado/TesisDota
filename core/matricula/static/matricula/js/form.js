var fvMatricula;

document.addEventListener('DOMContentLoaded', function (event) {
    const form = document.getElementById('frmForm');
    fvMatricula = FormValidation.formValidation(form, {
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
                estudiante: {
                    validators: {
                        notEmpty: {
                            message: 'Debe elegir al menos un estudiante..'
                        },
                        
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                
                                    obj: form.querySelector('[name="estudiante"]').value,
                                    type: 'estudiante',
                                    action: 'validate_data'
                                };
                            },
                            message: 'El estudiante ya se encuentra matriculado en este curso',
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
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
            const iconPlugin = fvMatricula.getPlugin('icon');
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
            var parameters = new FormData(fvMatricula.form);
            parameters.append('action', 'add');
            let urlrefresh = fvMatricula.form.getAttribute('data-url');
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

    

    $('select[name="estudiante"]').on('change', function (e) {
        fvMatricula.revalidateField('estudiante');
    });
    
});
